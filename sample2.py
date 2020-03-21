x = str(1.0) + "12.2" #1.0を文字型に
print(x)
print(type(x)) #xの型を調べる

#リスト
subject_name = ["国語","算数","理科","社会"] #リストか多変数の宣言
print(subject_name)
print(type(subject_name))
print(subject_name[1]) #算数を表示
print(subject_name[0:3]) #国語,算数,理科を表示

#末尾に追加　append
subject_name.append("追加") #リストに"追加"を追加
print(subject_name)

#もう一つのリストを追加、結合　extend
subject_name.extend(["追加A","追加B"]) #subject_nameにもう一つのリストを追加
print(subject_name)

#要素の割り込み　insert
subject_name.insert(2,"割り込み") #subject_nameリストの２番目に追加
print(subject_name)

#要素削除　remove
subject_name.remove("割り込み")
print(subject_name)

#要素変更　リスト名[リストNo]=
subject_name[0] = "Japanese"
print(subject_name)


#リスト(タプル型)　要素の変更が不可 []→()
sample_tuple = (10,20,"hello")
print(sample_tuple)
print(sample_tuple[1])

#セット　重複した要素を持てないタプル {}
sample_set = {10,100,"hello"}
print(sample_set)
