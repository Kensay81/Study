import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cats = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
def convert_list(cats):
    cats_list = []
    if isinstance(cats[0], tuple):
        for cat in cats:
            cats_list.append(cat._asdict())
    else:
        for cat in cats:
            cats_list.append(Cat(**cat))

    
    return cats_list

print(convert_list(cats))

