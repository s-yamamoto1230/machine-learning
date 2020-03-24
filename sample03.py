#辞書　辞書名 = {キー:バリュー１,・・・}
subject_dict = {"国語":70,"算数":80,"理科":100}
print(subject_dict)

#参照　辞書名["キー"]
print(subject_dict["算数"])

#追加　辞書名["追加するキー名"] = 追加する値
subject_dict["英語"] = 90
print(subject_dict)

#削除　辞書名.pop("消したいキー")
subject_dict.pop("英語")
print(subject_dict)

#変更　辞書名["変更するキー"] = 変更後の値
subject_dict["算数"] = 100
print(subject_dict)

#---------------------------------------------------
sato_dict = {"height":1.5,"weight":45}
BMI =sato_dict["weight"] / (sato_dict["height"] * sato_dict["height"])
print("佐藤さんのBMIは" + str(BMI) + "です")

x1 = 3.14
x2 = "3..14"
x3 = [3.14]
x4 = {"pi":3.14}
print(type(x1))
print(type(x2))
print(type(x3))
print(type(x4))
