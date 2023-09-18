def bread () :
    print ( " <////////// > " )
def lettuce () :
    print ( " ~~~~~~~~~~~~ " )
def tomato () :
    print ( " O O O O O O " )
def ham () :
    print ( " ============ " )

def prepare_sandwiches(num_sandwiches, vegetarian = False):
    for _ in range(num_sandwiches):
        bread()
        lettuce()
        tomato()
        if not vegetarian:
            ham()
            ham()
        tomato()
        lettuce()
        bread()
        print()

prepare_sandwiches(42, vegetarian=True)

prepare_sandwiches(42)