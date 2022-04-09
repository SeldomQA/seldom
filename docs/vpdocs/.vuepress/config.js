module.exports = {
  title: "seldom文档",
  description: "基于unittest 的 Web UI/HTTP自动化测试框架。",
  base: "/vpdocs/",
  // head: [["link", { rel: "icon", href: "/nuxt3-docs-zh/icon.png" }]],
  themeConfig: {
    repo: "/SeldomQA/seldom",
    // docsBranch: "master/docs",
    // logo: "/logo.svg",
    navbar: [
      { text: "指南", link: "/introduce" },
      { text: "更新日志", link: "https://github.com/SeldomQA/seldom" },
    ],
    sidebar: [
      "/introduce",
      {
        text: "开始",
        children: [
          "/getting-started/installation",
          "/getting-started/create_project",
          "/getting-started/quick_start",
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
