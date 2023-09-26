# # import random as r
# # link="workbook"
# # m=r.randint(10,100)
# # print(m)
# # s=str(link)+str(m)
# # print(s)
# from minio import Minio
# import random as r
# import io
# minio_client = Minio ("18.217.196.203:9000",
#                     "kBSeUX6rAW9Fj8LdohLi",
#                     "TNoS9XNLbXOv1LQTcH7Lsi9DXivlWN0oF4ApaKFT",
#                     secure=False)


# link="workbook_"
# m=r.randint(10,100)
# s=str(link)+str(m)
# with open("D:\Combined_views.pdf", "rb") as pdf_file:
#         pdf_data = pdf_file.read()
# minio_client.put_object("testing",f"{s}.pdf",io.BytesIO(pdf_data), len(pdf_data))
# pdf_url = minio_client.presigned_get_object("testing", f"{s}.pdf")

# print(pdf_url)


