import { readdir, readFile, stat } from "node:fs/promises";
import { join } from "node:path";

const root = new URL("..", import.meta.url).pathname;
const required = ["index.html", "daily/index.html", "daily/2026-06-29/index.html", "daily/2026-06-29/en/index.html", "assets/styles.css", "assets/app.js", "sitemap.xml"];
const missing = [];

for (const file of required) {
  try {
    await stat(join(root, file));
  } catch {
    missing.push(file);
  }
}

const htmlFiles = [];
async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = join(dir, entry.name);
    if (entry.isDirectory()) {
      await walk(full);
    } else if (entry.name.endsWith(".html")) {
      htmlFiles.push(full);
    }
  }
}

await walk(root);

const broken = [];
for (const file of htmlFiles) {
  const html = await readFile(file, "utf8");
  if (!html.includes("VLYQB1HXUW")) broken.push(file);
  if (!html.includes("/assets/styles.css?v=20260630-gate-blue")) broken.push(file);
}

if (missing.length || broken.length) {
  console.error({ missing, broken });
  process.exit(1);
}

console.log(`Checked ${htmlFiles.length} HTML files successfully.`);
