my_shopping_list = ["bread", "butter", "milk"]
# To remove the duplicate from the list -> Use "set" - data
print(my_shopping_list)
print(len(my_shopping_list))


def bring_more_food(my_list):
    more_item = input("enter your item\n")
    my_list.append("cheese")
    # my_list.remove(more_item)
    # my_list.insert(0, more_item)
    return my_list


L = bring_more_food(my_shopping_list)
print(L)
