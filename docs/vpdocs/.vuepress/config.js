import { searchPlugin } from '@vuepress/plugin-search'
import { backToTopPlugin } from '@vuepress/plugin-back-to-top'
import { defaultTheme } from "@vuepress/theme-default"


module.exports = {
  title: "seldom文档",
  description: "seldom 是基于unittest 的自动化测试框架。",
  base: "/",
  plugins: [
    searchPlugin({
      locales: {
        '/': {
          placeholder: 'Search',
        },
        '/zh/': {
          placeholder: '搜索',
        },
      },
    }),
    backToTopPlugin(),
  ],
  theme: defaultTheme({
    repo: "SeldomQA/seldom",
    docsBranch: "vuepress-docs/docs/vpdocs",
    logo: "/logo.jpeg",
    navbar: [
        { text: "介绍", link: "/introduce" },
        { text: "安装", link: "/getting-started/installation" },
    ],
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
          "/getting-started/seldom_cli",
        ],
      },
      {
        text: "web UI 测试",
        children: [
          "/web-testing/browser_driver",
          "/web-testing/seldom_api",
          "/web-testing/chaining",
          "/web-testing/page_object",
          "/web-testing/other",
        ],
      },
      {
        text: "App UI 测试",
        children: [
          "/app-testing/start",
          "/app-testing/appium_lab",
          "/app-testing/page_object",
        ],
      },
      {
        text: "HTTP接口测试",
        children: [
          "/api-testing/start",
          "/api-testing/assert",
          "/api-testing/more",
        ],
      },
      {
        text: "更多能力",
        children: [
          "/more-ability/db_operation",
          "/more-ability/test_library",
        ],
      },
      "/platform/platform",
      "/version/CHANGES",
    ],
    editLinks: true,
    editLinkText: "在 GitHub 上编辑此页",
    lastUpdated: "上次更新",
  })
};
