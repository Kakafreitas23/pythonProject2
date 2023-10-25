# # # import pandas as pd
# # #
# # # carros={"BMW":["Azul","Verde"],
# # #         "Ferrari":["Vermelha","Preta"],
# # #         "Porsche":["Amarela","Cinza"],
# # #         "Palio":["Branca","Roxa"]
# # #         }
# # # carros_df=pd.DataFrame(carros)
# # # print(carros_df)
# # #
# #
# # import pandas
# # Turmas={"1 ano":["Fita Amarela"],
# # 		"2 ano":["Fita Azul"],
# #         "3 ano":["Fita verde"]
# # }
# # Turmas_df=pandas.DataFrame(Turmas)
# # print(Turmas_df)
# #
# #
# # import pandas as pd
# # print(pd.__version__)
# #
# #
# # #Criando uma série pandas
# #
# # import pandas as pd
# #
# # calorias={ "Dia 1":250,
# #            "Dia 2":400,
# #            "Dia 3":600,
# #            "Dia 4":800
# # }
# # calorias_df=pd.Series(calorias)
# # print(calorias_df)
# #
# # #Use o index de argumento
# #
# # import pandas as pd
# #
# # calorias={ "Dia 1":250,
# #            "Dia 2":400,
# #            "Dia 3":600,
# #            "Dia 4":800}
# # calorias_df=pd.Series(calorias,index=["Dia 1","Dia 2"])
# # print(calorias_df)
# #
#
# #Index em uma série pandas
#
# import pandas as pd
# calorias={ "Dia 1":250,
#            "Dia 2":400,
#            "Dia 3":600,
#            "Dia 4":800
# }
# valores_calorias=pd.Series(calorias,index=["Dia 3","Dia 4"])
# print(valores_calorias)
#
# import pandas as pd
# calorias={ "Dia 1":250,
#            "Dia 2":400,
#            "Dia 3":600,
#            "Dia 4":800
# }
# calorias_achadas=pd.Series(calorias,index=["Dia 2","Dia 4"])
# print(calorias_achadas)

#Dataframe de duas séries

import pandas as pd
data={
    "calorias":[400,800,600],
    "Duração":[50,20,45]
}
data_df=pd.DataFrame(data)
print(data_df)

#print(data_df.loc[[2,1]])




























