import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";
import mdx from "@astrojs/mdx";
import robotsTxt from "astro-robots-txt";
import { SITE_URL } from "./src/data/config";
import rehypePrettyCode from "rehype-pretty-code";
import remarkToc from "remark-toc";



export default defineConfig({
  integrations: [mdx(), tailwind(), sitemap(), robotsTxt()],
  site: SITE_URL,
  markdown: {
    syntaxHighlight: false,
    remarkPlugins: [remarkToc],
    rehypePlugins: [rehypePrettyCode]
  }
});
