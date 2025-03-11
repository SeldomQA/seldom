# 确保脚本抛出遇到的错误
set -e

# 生成静态文件
npm run build

# 进入生成的文件夹
cd vpdocs/.vuepress/dist

git init
git add -A
git commit -m 'deploy'

# 如果发布到 https://SeldomQA.github.io
git push -f https://github.com/SeldomQA/SeldomQA.github.io.git master
cd -
