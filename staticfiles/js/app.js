// igstats interface behaviour. No dependencies; every block is a no-op when
// its markup is absent, so the same file serves every page.
(() => {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  // Theme toggle (initial theme is set inline in <head> to avoid a flash).
  $$("[data-theme-toggle]").forEach((btn) =>
    btn.addEventListener("click", () => {
      const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      document.documentElement.dataset.theme = next;
      try { localStorage.setItem("theme", next); } catch (e) {}
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

  // Busy state on analyze submit.
  $$("[data-analyze-form]").forEach((form) =>
    form.addEventListener("submit", () => {
      const btn = $("[data-submit]", form);
      btn.dataset.label = $("[data-label]", btn).textContent;
      btn.dataset.icon = $("[data-icon]", btn).innerHTML;
      btn.disabled = true;
      $("[data-label]", btn).textContent = btn.dataset.busyLabel;
      $("[data-icon]", btn).innerHTML = '<span class="spinner"></span>';
    })
  );
  // Re-enable submit buttons when the page comes back from the back/forward cache.
  window.addEventListener("pageshow", (e) => {
    if (!e.persisted) return;
    $$("[data-analyze-form] [data-submit]").forEach((btn) => {
      btn.disabled = false;
      $("[data-label]", btn).textContent = btn.dataset.label;
      $("[data-icon]", btn).innerHTML = btn.dataset.icon;
    });
  });

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
