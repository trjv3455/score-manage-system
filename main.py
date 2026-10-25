"""
学生成绩管理系统
功能：添加学生、查询学生、按成绩升序/降序排序、统计平均分、展示全部
"""

students = []

def add_student():
    name = input("请输入学生姓名：")
    try:
        score = float(input("请输入学生成绩："))
    except ValueError:
        print("成绩输入非法！")
        return
    students.append({"name": name, "score": score})
    print(f"【成功】已添加：{name}，成绩：{score}")

def search_by_name():
    target = input("输入要查找的学生姓名：")
    res = [s for s in students if s["name"] == target]
    if res:
        for s in res:
            print(f"找到：{s['name']} | 成绩：{s['score']}")
    else:
        print("未找到该学生")

def sort_by_score():
    order = input("1-升序，2-降序：")
    if order == "1":
        sorted_list = sorted(students, key=lambda x: x["score"])
    elif order == "2":
        sorted_list = sorted(students, key=lambda x: x["score"], reverse=True)
    else:
        print("输入选项错误")
        return
    print("\n===== 排序结果 =====")
    for s in sorted_list:
        print(f"{s['name']} : {s['score']}")

def calc_avg():
    if not students:
        print("暂无学生数据")
        return
    total = sum(s["score"] for s in students)
    avg = total / len(students)
    print(f"学生总数：{len(students)}，平均分：{avg:.2f}")

def show_all():
    if not students:
        print("暂无学生")
        return
    print("\n===== 全部学生 =====")
    for s in students:
        print(f"{s['name']} | {s['score']}")

def menu():
    while True:
        print("\n===== 成绩管理系统 =====")
        print("1. 添加学生")
        print("2. 按姓名查找")
        print("3. 成绩排序")
        print("4. 计算平均分")
        print("5. 查看全部学生")
        print("0. 退出")
        opt = input("请选择功能：")
        if opt == "1":
            add_student()
        elif opt == "2":
            search_by_name()
        elif opt == "3":
            sort_by_score()
        elif opt == "4":
            calc_avg()
        elif opt == "5":
            show_all()
        elif opt == "0":
            print("程序退出")
            break
        else:
            print("无效选项")

if __name__ == "__main__":
    menu()
