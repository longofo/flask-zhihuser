FROM python:3.6

RUN apt-get -y update

WORKDIR /zhihu-flask

COPY ./zhihuuser /zhihu-flask

RUN pip install --upgrade pip && \
            pip install -r ./requirements/requirements.txt

# FLASKY_PER_PAGE: 每页显示的用户数
# FLASKY_ADMIN: 管理员
# MONGO_URI: mongo连接地址
ENV FLASKY_PER_PAGE=20 \
            FLASKY_ADMIN='test@qq.com'  \
            MONGO_URI='mongodb://zhihu-mongo:27017/zhihu'

ENTRYPOINT ["python","manager.py","runserver","--host=0.0.0.0"]
