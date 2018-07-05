class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        for item in self.slots:
            # yield works like return but it doesn't end the execution of the method.
            # it lets us send values back out of the functon/method as they are available and keep working
            # this is known as a generator
            yield item
        # alternative way of writing this:
        # yield from self.slots