module.exports = {
  title: "seldom文档",
  description: "基于unittest 的 Web UI/HTTP自动化测试框架。",
  base: "/",
  plugins: [
    [
      "@vuepress/plugin-search",
      {
        locales: {
          "/": {
            placeholder: "Search",
          },
          "/zh/": {
            placeholder: "搜索",
          },
        },
         isSearchable: (page) => page.path !== '/',
      },
    ],
  ],
  themeConfig: {
    repo: "SeldomQA/seldom",
    docsBranch: "vuepress-docs/docs/vpdocs",
    logo: "/logo.jpeg",
    navbar: [{ text: "指南", link: "/introduce" }],
    sidebar: [
      "/introduce",
      {
        text: "开始",
        children: [
          "/getting-started/installation",
          "/getting-started/create_project",
          "/getting-started/quick_start",
          "/getting-started/advanced",
          "/getting-started/data_driver",
        ],
      },
      {
        text: "进阶",
        children: [
          "/advanced/seldom_api",
          "/advanced/chaining",
          "/advanced/advanced",
        ],
      },
      "/other/other",
      "/http/http",
      "/db/db_operation",
      "/platform/platform",
    ],
    editLinks: true,
    editLinkText: "在 GitHub 上编辑此页",
    lastUpdated: "上次更新",
  },
};
