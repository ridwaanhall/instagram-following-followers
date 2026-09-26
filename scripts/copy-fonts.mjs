// Copy the latin + latin-ext variable woff2 files from @fontsource-variable into
// staticfiles/font, so the site never loads a font from a third-party host.
import { copyFileSync, mkdirSync, readdirSync, rmSync } from "node:fs";
import { join } from "node:path";

// family -> axis file to use ("opsz" files carry both the wght and opsz axes).
const families = { newsreader: "opsz", "schibsted-grotesk": "wght", "geist-mono": "wght" };
const out = "staticfiles/font";

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });

for (const [family, axis] of Object.entries(families)) {
  const dir = join("node_modules/@fontsource-variable", family, "files");
  const pattern = new RegExp(`-latin(-ext)?-${axis}-normal\.woff2$`);
  for (const file of readdirSync(dir).filter((f) => pattern.test(f))) {
    copyFileSync(join(dir, file), join(out, file));
    console.log(`font: ${file}`);
  }
}
