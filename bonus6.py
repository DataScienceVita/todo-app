# contents = ["All carrots are to be sliced longitudinally.", "The carrots were reportedly sliced.", "The slicing process was well presented."]
#  if the above is too long use below for multiple lines of code as a single expression

contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    # file = open(f"../files/{filename}", 'w') # creating the files in one level of directory above a folder
    file = open(f"files/{filename}", 'w')
    file.write(content)


