store = Gtk.ListStore(str, str, float)

treeiter = store.append(["The Art of Computer Programming",
						"Donald E. Knuth", 25.46])

print(store[treeiter][2]) # Prints value of third column
store[treeiter][2] =  42.15

# Print number of rows
print(len(store))
# print all but first column
print(stroe[treeiter][1:])
# print last column
print(store[treeiter][-1])
# set last two columns
store[treeiter][1:] = ["Donald Ervin Knuth", 41.99]

for row in store:
	# Print values of all columns
	print(row[:])

def print_tree_store(store):
	rootiter = store.get_iter_first()
	print_rows(store, rootiter, "")

def print_rows(store, treeiter, indent):
	while treeiter is not None:
		print(indent + str(store[treeiter][:]))
		if store.iter_has_child(treeiter):
			childiter = store.iter_children(treeiter)
			print_rows(store, childiter, indent + "\t")
		treeiter = store.iter_next(treeiter)

# Get path pointing to 6th row in list store
path = Gtk.TreePath(5)
treeiter = liststore.get_iter(path)
# Get value at 2nd column
value = liststore.get_Value(treeiter, 1)
# Get path pointing to 5th child of 3rd row in tree store
path = Gtk.TreePath([2, 4])
treeiter = treestore.get_iter(path)
# Get value at 2nd column
value = treestore.get_Value(treeiter, 1)

tree = Gtl.TreeView(store)

renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Title", renderer, text=0)
tree.append_column(column)

column = Gtk.TreeViewColumn("Title and Author")

title = Gtk.CellRendererText()
author = Gtk.CellRendererText()

column.pack_start(title, True)
column.pack_start(author, True)

column.add_attribute(title, "text", 0)
column.add_attribute(author, "text", 1)

tree.append_column(column)


select = tree.get_selection()
select.connect("changed", on_tree_selection_changed)

def on_tree_selection_changed(selection):
	model, treeiter = selection.get_selected()
	if treeiter is not None:
		print("You selected", model[treeiter][0])


model = Gtk.ListStore(str)
model.append(["Benjamin"])
model.append(["Charles"])
model.append(["alfred"])
model.append(["Alfred"])
model.append(["David"])
model.append(["charles"])
model.append(["david"])
model.append(["benjamin"])

treeView = Gtk.TreeView(model)

cellRenderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Title", renderer, text=0)

column.set_sort_column_id(0)

def compare(model, row1, row2, user_data):
	sort_column,_=model.get_sort_column_id()
	value1 = model.get_value(row1, sort_column)
	value2 = model.get_value(row2, sort_column)
	if value1 < value2:
		return -1
	elif value1 == value2:
		return 0
	else: 
		return 1

model.set_sort_func(0, compare, None)

filter = model.filter_new()
filter.set_visible_func(filter_func, data=None)
