class Graphs:
    def __init__(self, edges):
        self.edges = edges
        self.dict = {}

        for start, end in self.edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]
        print('Dictionary: ', self.dict)

    def get_paths(self, start, end, path = []):

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.dict:
            return []

        possible = []

        for node in self.dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for x in new_path:
                    possible.append(x)

        return possible

    def shortest(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return path

        if start not in self.dict:
            return None

        shortest = None

        for node in self.dict[start]:
            if node not in path:
                sp = self.shortest(node, end, path)
                if sp:
                    if shortest is None or len(sp) < len(shortest):
                        shortest = sp

        return shortest


routes = [
    ('Cape Town', 'Paris'),
    ('Cape Town', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto'),
]

path = Graphs(routes)
print('')

strt = input('Enter starting destination:')
dstn = input('Enter your end destination:')

print(path.get_paths(strt, dstn))
print('')
print(path.shortest(strt, dstn))
