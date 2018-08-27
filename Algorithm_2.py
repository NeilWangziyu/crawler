from collections import deque


def person_is_seller(person):
    if person[-1] == 'm':
        return True
    else:
        return False

def find_the_seller(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person, 'is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('none of them is a mango seller')
    return False

if __name__ == '__main__':
    graph = {}
    graph['you'] = ['alice', "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []



    find_the_seller('you')
