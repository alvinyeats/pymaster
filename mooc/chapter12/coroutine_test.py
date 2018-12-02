# _*_ coding: utf-8 _*_


def gen_func():
    html = yield
    print(html)
    yield 2
    yield 3
    return "finish"


if __name__ == "__main__":
    gen = gen_func()
    # 在调用send发送非none值之前，我们必须启动一次生成器，方式有两种
    url = next(gen)
    html = "alvin"
    print(gen.send(html))
    print(next(gen))


