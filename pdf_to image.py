from pdf2image import convert_from_path

old_pdf = convert_from_path(r"D:\Anjali\College\Semesters\B Tech IT-2023 Course Sem-I to VI Syllabus 19-4-2025.pdf",
                            poppler_path=r"D:\Anjali\College\python\projects\pdf_to_image\poppler-25.07.0\Library\bin")
for i in range(len(old_pdf)):
    old_pdf[i].save("new"+str(i)+".jpg","JPEG")