def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数: lst - 任意列表
    返回: bool - 如果有重复元素返回 True，否则返回 False
    """
    seen = set()
    for element in lst:
        if element in seen:
            return True
        seen.add(element)
    return False


# 主程序 - 测试函数
if __name__ == "__main__":
    # 学生需要提供测试用例
    test_cases = [
        [1, 2, 3],          # 无重复
        [1, 2, 2],          # 有重复
        ["a", "b", "a"],    # 字符串重复
        []                   # 空列表
    ]

    for case in test_cases:
        result = has_duplicates(case)
        print(f"列表 {case} 是否有重复元素: {result}")
