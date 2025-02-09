# ベースイメージを指定
FROM node:22.13.1

# node.js の環境変数を定義する
# 本番環境では production
ENV NODE_ENV=development

# ディレクトリを移動する
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./

# 雛形を生成するのに必要なパッケージのインストール
RUN npm install -g nodemon

# ポート3000番を開放する
EXPOSE 3000
CMD ["nodemon sydpower-run.js"]