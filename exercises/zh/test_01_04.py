def test():
    assert (
        "if next_token.like_num" in __solution__
    ), "你有检查下一个词符的like_num属性了吗？"
    assert (
        'token.text == "￥"' in __solution__
    ), "你有检查词符的文本是￥了吗？"
    assert (
        token.text == "￥"
    ), "你有检查词符的文本是￥了吗？"

    __msg__.good(
        "太棒了！你也看到了，我们可以用词符和其属性"
        "进行很多很强大的分析！"
    )
