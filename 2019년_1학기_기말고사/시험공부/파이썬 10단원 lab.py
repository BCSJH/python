# 노트북 프로그램 만들기
# 노트 정리하는 프로그램
# 사용자는 노트에 콘텐츠를 적기 가능
# 노트북은 타이틀이 있음
# 노트북은 노트가 삽입될 때 페이지를 생성하며, 최대 300페이지까지 저장하근ㅇ
# 300페이지를 넘기면 노트를 더는 삽입하지 못함

#note 클래스
class Note(object):
    def __init__(self,contents = None):
        self.contents = contents

    def write_contents(self, contents):
        self.contents = contents

    def remove_all(self):
        self.contents = ""

    def __str__ (self):
        return self.contents


class Notebook(object):
    def __init__(self,title):
        self.title = title
        self.page_number=1
        self.notes = {}

    def add_note(self,note,page=0):
        if self.page_number < 300:
            if page ==0:
                self.notes[self.page_number] = note
                self.page_number +=1
            else:
                self.notes = {page:note}
                self.page_number +=1
        else:
            print("페이지가 모두 채워졌다.")
    def remove_note(self,page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않는다.")
    def get_number_of_pages(self):
        return len(self.notes.keys())


good_notebook = "세상을 사는 데 도움이 되는 명언, 힘이되는 명언, 용기를 주는 명언, 위로되는 명언, 좋은 명언 모음 100가지, 자주 보면 좋을 것 같아 선별했습니다."
note_1 = Note(good_notebook)
print(note_1)
note_1.remove_all()
print(note_1)

wish_saying_notebook = Notebook("명언 노트")
wish_saying_notebook.add_note(note_1)
wish_saying_notebook.add_note(note_1)
wish_saying_notebook.add_note(note_1)
wish_saying_notebook.add_note(note_1)
print(wish_saying_notebook)
print(wish_saying_notebook.get_number_of_pages())

wish_saying_notebook.add_note(note_1,100)

wish_saying_notebook.add_note(note_1,100)