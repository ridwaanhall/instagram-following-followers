// igstats interface behaviour. No dependencies; every block is a no-op when
// its markup is absent, so the same file serves every page.
(() => {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Theme toggle (initial theme is set inline in <head> to avoid a flash).
  // .theme-switching stops every per-element colour transition so the page
  // flips as one; the View Transition then cross-fades old and new states.
  const root = document.documentElement;
  const setTheme = (next) => {
    root.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (e) {}
  };
  $$("[data-theme-toggle]").forEach((btn) =>
    btn.addEventListener("click", () => {
      const next = root.dataset.theme === "dark" ? "light" : "dark";
      root.classList.add("theme-switching");
      const done = () => requestAnimationFrame(() => root.classList.remove("theme-switching"));
      if (document.startViewTransition && !reduceMotion) {
        document.startViewTransition(() => setTheme(next)).finished.finally(done);
      } else {
        setTheme(next);
        requestAnimationFrame(done);
      }
    })
  );

  // Mobile menu.
  const menuBtn = $("[data-menu-toggle]");
  const menu = $("#mobile-menu");
  if (menuBtn && menu) {
    const setMenu = (open) => {
      menu.hidden = !open;
      menuBtn.setAttribute("aria-expanded", String(open));
      $("[data-menu-open]", menuBtn).hidden = open;
      $("[data-menu-close]", menuBtn).hidden = !open;
    };
    menuBtn.addEventListener("click", () => setMenu(menu.hidden));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !menu.hidden) { setMenu(false); menuBtn.focus(); } });
    matchMedia("(min-width: 768px)").addEventListener("change", (e) => e.matches && setMenu(false));
  }

  // <details> dropdowns close on outside click and Escape.
  const dropdowns = $$("[data-dropdown]");
  document.addEventListener("click", (e) => dropdowns.forEach((d) => { if (!d.contains(e.target)) d.open = false; }));
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    dropdowns.forEach((d) => { if (d.open) { d.open = false; $("summary", d).focus(); } });
  });

  // Custom select: the native <select> stays in the DOM as the source of truth
  // (and the no-JS fallback); a button + ARIA listbox replaces it visually.
  const CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>';
  const CHECK = '<svg class="check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>';
  let selectId = 0;
  $$("[data-select]").forEach((wrap) => {
    const select = $("select", wrap);
    const id = `select-${++selectId}`;
    const options = Array.from(select.options);

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "select-trigger";
    trigger.setAttribute("aria-haspopup", "listbox");
    trigger.setAttribute("aria-expanded", "false");
    trigger.setAttribute("aria-controls", `${id}-list`);
    trigger.setAttribute("aria-label", select.getAttribute("aria-label") || "");
    trigger.innerHTML = `<span class="truncate" data-value></span>${CHEV}`;

    const list = document.createElement("ul");
    list.id = `${id}-list`;
    list.className = "select-list";
    list.setAttribute("role", "listbox");
    list.setAttribute("tabindex", "-1");
    list.setAttribute("aria-label", select.getAttribute("aria-label") || "");
    list.hidden = true;
    options.forEach((opt, i) => {
      const li = document.createElement("li");
      li.id = `${id}-opt-${i}`;
      li.className = "select-option";
      li.setAttribute("role", "option");
      li.dataset.value = opt.value;
      li.innerHTML = `<span></span>${CHECK}`;
      li.firstChild.textContent = opt.textContent;
      list.appendChild(li);
    });
    const items = $$('[role="option"]', list);

    select.hidden = true;
    select.tabIndex = -1;
    $(".select-chev", wrap)?.remove();
    wrap.append(trigger, list);

    let active = 0;
    const setActive = (i) => {
      active = (i + items.length) % items.length;
      items.forEach((li, j) => li.classList.toggle("is-active", j === active));
      list.setAttribute("aria-activedescendant", items[active].id);
      items[active].scrollIntoView({ block: "nearest" });
    };
    const sync = () => {
      items.forEach((li) => li.setAttribute("aria-selected", String(li.dataset.value === select.value)));
      $("[data-value]", trigger).textContent = select.options[select.selectedIndex].textContent;
    };
    const open = () => {
      list.hidden = false;
      const below = window.innerHeight - trigger.getBoundingClientRect().bottom;
      list.toggleAttribute("data-up", below < list.offsetHeight + 16);
      trigger.setAttribute("aria-expanded", "true");
      setActive(select.selectedIndex);
      list.focus({ preventScroll: true });
    };
    const close = (focus = true) => {
      if (list.hidden) return;
      list.hidden = true;
      trigger.setAttribute("aria-expanded", "false");
      if (focus) trigger.focus();
    };
    const choose = (i) => {
      if (select.selectedIndex !== i) {
        select.selectedIndex = i;
        select.dispatchEvent(new Event("change", { bubbles: true }));
      }
      sync();
      close();
    };

    trigger.addEventListener("click", () => (list.hidden ? open() : close()));
    trigger.addEventListener("keydown", (e) => {
      if (["ArrowDown", "ArrowUp", "Enter", " "].includes(e.key)) { e.preventDefault(); open(); }
    });
    list.addEventListener("keydown", (e) => {
      const keys = {
        ArrowDown: () => setActive(active + 1),
        ArrowUp: () => setActive(active - 1),
        Home: () => setActive(0),
        End: () => setActive(items.length - 1),
        Enter: () => choose(active),
        " ": () => choose(active),
        Escape: () => close(),
      };
      if (keys[e.key]) { e.preventDefault(); keys[e.key](); return; }
      if (e.key === "Tab") { close(false); return; }
      if (e.key.length === 1) {
        const from = active + 1;
        const k = e.key.toLowerCase();
        const hit = items.map((_, j) => (from + j) % items.length).find((j) => items[j].textContent.trim().toLowerCase().startsWith(k));
        if (hit !== undefined) setActive(hit);
      }
    });
    items.forEach((li, i) => {
      li.addEventListener("mousemove", () => { if (active !== i) setActive(i); });
      li.addEventListener("click", () => choose(i));
    });
    document.addEventListener("pointerdown", (e) => { if (!wrap.contains(e.target)) close(false); });
    select.addEventListener("change", sync);
    sync();
  });

  // Dismissible alerts.
  $$("[data-dismiss]").forEach((btn) => btn.addEventListener("click", () => btn.closest("[data-dismissible]").remove()));

  // Tabs: click or arrow keys; tabs may be links, which still work without JS.
  $$("[data-tabs]").forEach((root) => {
    const tabs = $$('[role="tab"]', root);
    const select = (tab, focus) => {
      if (root.hasAttribute("data-tabs-links")) return tab.focus();
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        const panel = $(`[data-panel="${t.dataset.tab}"]`, root);
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
      root.dispatchEvent(new CustomEvent("tabchange", { detail: tab.dataset.tab }));
    };
    tabs.forEach((tab, i) => {
      tab.addEventListener("click", (e) => {
        if (root.hasAttribute("data-tabs-links")) return; // method pages: follow the link
        e.preventDefault();
        select(tab);
      });
      tab.addEventListener("keydown", (e) => {
        const step = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (step) { e.preventDefault(); select(tabs[(i + step + tabs.length) % tabs.length], true); }
        if (e.key === "Home") { e.preventDefault(); select(tabs[0], true); }
        if (e.key === "End") { e.preventDefault(); select(tabs[tabs.length - 1], true); }
      });
    });
  });

  // Dropzones: show the chosen file name and a drag state.
  $$("[data-dropzone]").forEach((zone) => {
    const input = $("[data-file-input]", zone);
    const name = $("[data-drop-name]", zone);
    const placeholder = name.textContent;
    const update = () => {
      const file = input.files && input.files[0];
      zone.classList.toggle("has-file", !!file);
      name.textContent = file ? `${file.name} · ${(file.size / 1024).toFixed(file.size > 1048576 ? 0 : 1)} KB` : placeholder;
    };
    input.addEventListener("change", update);
    ["dragenter", "dragover"].forEach((ev) => zone.addEventListener(ev, () => zone.classList.add("is-dragging")));
    ["dragleave", "drop"].forEach((ev) => zone.addEventListener(ev, () => zone.classList.remove("is-dragging")));
    update();
  });

  // Live JSON validation for the paste tab.
  $$("[data-json-input]").forEach((area) => {
    const status = document.getElementById(area.getAttribute("aria-describedby"));
    const dot = $("[data-dot]", status);
    const text = $("[data-text]", status);
    const check = () => {
      const value = area.value.trim();
      let state = "waiting";
      if (value) { try { JSON.parse(value); state = "valid"; } catch (e) { state = "invalid"; } }
      text.textContent = status.dataset[state];
      dot.className = "size-1.5 rounded-full " + { waiting: "bg-ink-3", valid: "bg-ink", invalid: "bg-accent" }[state];
      area.setAttribute("aria-invalid", String(state === "invalid"));
    };
    area.addEventListener("input", check);
    check();
  });

  // Analyze forms: validate before sending (native bubbles are off via
  // novalidate), then show a busy state. The server validates again.
  const fieldError = (field) => {
    if (field.type === "file") {
      const file = field.files && field.files[0];
      if (!file) return field.dataset.errEmpty;
      const exts = (field.dataset.ext || "").split(" ").filter(Boolean);
      if (exts.length && !exts.some((ext) => file.name.toLowerCase().endsWith(ext))) return field.dataset.errType;
      return null;
    }
    const value = field.value.trim();
    if (!value) return field.dataset.errEmpty;
    try { JSON.parse(value); } catch (e) { return field.dataset.errType; }
    return null;
  };
  const markField = (field, bad) => {
    const zone = field.closest("[data-dropzone]");
    if (zone) zone.classList.toggle("is-invalid", bad);
    else field.setAttribute("aria-invalid", String(bad));
  };
  $$("[data-analyze-form]").forEach((form) => {
    const box = $("[data-form-error]", form);
    const list = $("[data-form-error-list]", form);
    const fields = $$("[data-err-empty]", form);
    const clear = (field) => {
      markField(field, false);
      if (fields.every((f) => !fieldError(f))) box.hidden = true;
    };
    fields.forEach((f) => f.addEventListener(f.type === "file" ? "change" : "input", () => clear(f)));

    form.addEventListener("submit", (e) => {
      const errors = fields.map((f) => [f, fieldError(f)]).filter(([, msg]) => msg);
      fields.forEach((f) => markField(f, false));
      if (errors.length) {
        e.preventDefault();
        list.replaceChildren(...errors.map(([f, msg]) => {
          markField(f, true);
          return Object.assign(document.createElement("li"), { textContent: msg });
        }));
        const wasHidden = box.hidden;
        box.hidden = false;
        if (!wasHidden && !reduceMotion) {
          box.classList.remove("is-nudging");
          void box.offsetWidth;
          box.classList.add("is-nudging");
        }
        box.focus({ preventScroll: true });
        box.scrollIntoView({ block: "nearest", behavior: reduceMotion ? "auto" : "smooth" });
        return;
      }
      box.hidden = true;
      const btn = $("[data-submit]", form);
      btn.dataset.label = $("[data-label]", btn).textContent;
      btn.dataset.icon = $("[data-icon]", btn).innerHTML;
      btn.disabled = true;
      $("[data-label]", btn).textContent = btn.dataset.busyLabel;
      $("[data-icon]", btn).innerHTML = '<span class="spinner"></span>';
    });
  });
  // Re-enable submit buttons when the page comes back from the back/forward cache.
  window.addEventListener("pageshow", (e) => {
    if (!e.persisted) return;
    $$("[data-analyze-form] [data-submit]").forEach((btn) => {
      btn.disabled = false;
      $("[data-label]", btn).textContent = btn.dataset.label;
      $("[data-icon]", btn).innerHTML = btn.dataset.icon;
    });
  });

  // Scroll reveal: sections fade up once as they enter the viewport.
  const reveals = $$("[data-reveal]");
  if (reveals.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      reveals.forEach((el) => el.classList.add("is-in"));
    } else {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
        });
      }, { rootMargin: "0px 0px -10% 0px" });
      reveals.forEach((el) => io.observe(el));
    }
  }

  // Results figures count up from zero.
  if (!reduceMotion) {
    $$("[data-count]").forEach((el) => {
      const target = parseInt(el.textContent.replace(/\D/g, ""), 10);
      if (!target) return;
      const start = performance.now();
      const duration = Math.min(1100, 500 + target * 4);
      const tick = (now) => {
        const t = Math.min(1, (now - start) / duration);
        el.textContent = String(Math.round(target * (1 - Math.pow(1 - t, 3))));
        if (t < 1) requestAnimationFrame(tick);
      };
      el.textContent = "0";
      requestAnimationFrame(tick);
    });
  }

  // Chart tooltips: hover or keyboard focus on a month column.
  $$("[data-chart]").forEach((chart) => {
    const tip = $("[data-chart-tip]", chart);
    const show = (col) => {
      $("[data-tip-title]", tip).textContent = col.dataset.tipTitle;
      $("[data-tip-a]", tip).textContent = col.dataset.tipA;
      $("[data-tip-b]", tip).textContent = col.dataset.tipB;
      tip.hidden = false;
      const box = chart.getBoundingClientRect();
      const c = col.getBoundingClientRect();
      const half = tip.offsetWidth / 2;
      const x = Math.min(Math.max(c.left - box.left + c.width / 2, half), box.width - half);
      tip.style.left = `${x}px`;
      tip.style.top = `${Math.max(0, c.top - box.top - tip.offsetHeight + 8)}px`;
    };
    const hide = () => { tip.hidden = true; };
    $$(".chart-col", chart).forEach((col) => {
      col.addEventListener("pointerenter", () => show(col));
      col.addEventListener("focus", () => show(col));
      col.addEventListener("pointerleave", hide);
      col.addEventListener("blur", hide);
    });
    window.addEventListener("resize", hide);
  });

  // Reload button on the 500 page (no inline handlers: the CSP forbids them).
  $$("[data-reload]").forEach((btn) => btn.addEventListener("click", () => location.reload()));

  // Print.
  $$("[data-print]").forEach((btn) => btn.addEventListener("click", () => window.print()));

  // Results: search, sort, copy, CSV export on the active list.
  const results = $("[data-results]");
  if (results) {
    const search = $("[data-search]", results);
    const sort = $("[data-sort]", results);
    const noMatch = $("[data-no-match]", results);
    const activePanel = () => $("[data-panel]:not([hidden])", results);
    const rows = (panel) => $$("[data-username]", panel);
    const visibleRows = () => rows(activePanel()).filter((r) => !r.hidden);

    const apply = () => {
      const panel = activePanel();
      const list = $("[data-list]", panel);
      const q = search.value.trim().toLowerCase().replace(/^@/, "");
      const all = rows(panel);
      if (list) {
        const sorted = all.slice().sort((a, b) => {
          if (sort.value === "az") return a.dataset.username.localeCompare(b.dataset.username);
          const d = Number(a.dataset.ts) - Number(b.dataset.ts);
          return sort.value === "oldest" ? d : -d;
        });
        sorted.forEach((r) => list.appendChild(r));
      }
      let shown = 0;
      all.forEach((r) => { r.hidden = q && !r.dataset.username.toLowerCase().includes(q); if (!r.hidden) shown++; });
      $("[data-visible-count]", panel).textContent = q ? `${shown} / ${all.length}` : String(all.length);
      noMatch.classList.toggle("hidden", !(q && all.length && !shown));
      if (list) list.hidden = q && !shown;
    };
    search.addEventListener("input", apply);
    sort.addEventListener("change", apply);
    results.addEventListener("tabchange", apply);

    const copyBtn = $("[data-copy]", results);
    copyBtn.addEventListener("click", async () => {
      const names = visibleRows().map((r) => r.dataset.username).join("\n");
      if (!names) return;
      try {
        await navigator.clipboard.writeText(names);
      } catch (e) {
        // Fallback for contexts without clipboard permission.
        const area = Object.assign(document.createElement("textarea"), { value: names });
        area.style.cssText = "position:fixed;opacity:0";
        document.body.appendChild(area);
        area.select();
        const ok = document.execCommand("copy");
        area.remove();
        if (!ok) return;
      }
      const label = $("[data-copy-text]", copyBtn);
      const original = label.textContent;
      const icon = $("[data-copy-icon]", copyBtn);
      const originalIcon = icon.innerHTML;
      label.textContent = copyBtn.dataset.copiedLabel;
      icon.innerHTML = '<svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>';
      setTimeout(() => { label.textContent = original; icon.innerHTML = originalIcon; }, 1600);
    });

    $("[data-export]", results).addEventListener("click", () => {
      const panel = activePanel();
      const esc = (v) => `"${String(v).replace(/"/g, '""')}"`;
      const lines = [["username", "profile_url", "date"].join(",")].concat(
        visibleRows().map((r) => [r.dataset.username, r.dataset.href, r.dataset.date].map(esc).join(","))
      );
      const blob = new Blob(["﻿" + lines.join("\r\n")], { type: "text/csv;charset=utf-8" });
      const a = Object.assign(document.createElement("a"), {
        href: URL.createObjectURL(blob),
        download: `igstats-${panel.dataset.panel}-${new Date().toISOString().slice(0, 10)}.csv`,
      });
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 1000);
    });
  }

  // Privacy: highlight the section in view.
  const tocLinks = $$("[data-toc-link]");
  if (tocLinks.length && "IntersectionObserver" in window) {
    const byId = Object.fromEntries(tocLinks.map((a) => [a.hash.slice(1), a]));
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        tocLinks.forEach((a) => a.classList.remove("!text-ink"));
        const link = byId[entry.target.id];
        if (link) link.classList.add("!text-ink");
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    $$("[data-toc-section]").forEach((s) => observer.observe(s));
  }
})();
