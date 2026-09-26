// Copy the latin + latin-ext variable woff2 files from @fontsource-variable into
// staticfiles/font, so the site never loads a font from a third-party host.
import { copyFileSync, mkdirSync, readdirSync, rmSync } from "node:fs";
import { join } from "node:path";

const families = ["bricolage-grotesque", "hanken-grotesk", "jetbrains-mono"];
const out = "staticfiles/font";

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });

for (const family of families) {
  const dir = join("node_modules/@fontsource-variable", family, "files");
  for (const file of readdirSync(dir)) {
    if (/-latin(-ext)?-wght-normal\.woff2$/.test(file)) {
      copyFileSync(join(dir, file), join(out, file));
      console.log(`font: ${file}`);
    }
  }
}
