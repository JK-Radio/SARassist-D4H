#!python

orgs = [
  {
    "name": "BCSARA",
    "id": "CC3A9DC9-01A3-4D39-B806-2128B51120BC"
  },
  {
    "name": "ABSAR",
    "id": "14CC75FE-75D3-44EE-B622-0C0727160675"
  },
  {
    "name": "OtherOrgs",
    "id": "D2BB4ADB-13FE-4941-AB4A-1A5020C3DC8C"
  },
  {
    "name": "SARVAC",
    "id": "2c7b4d1b-151e-4315-b4c9-f7c810568b2f"
  },
  {
    "name": "Euro",
    "id": "62d294f8-73cc-4957-b43a-a03d886d3bbe"
  },
  {
    "name": "Portugal",
    "id": "0948300a-bca0-4338-a5fc-f08402120498"
  },
  {
    "name": "NCSAR",
    "id": "806b2639-403b-473f-bba8-3b247ad3175a"
  },
  {
    "name": "NBSAR",
    "id": "fa0eea08-7d7f-4f71-af1b-1ae8b38e2566"
  },
  {
    "name": "LE",
    "id": "2a164b90-4364-4de3-b9ef-457555df5855"
  },
  {
    "name": "GA",
    "id": "30307d12-ff30-48bc-bb0e-1d06899f228a"
  }
]

teams = [
  {
    "id": "46698CE0-B146-40E2-B834-0089DECE3896",
    "org": "BCSARA",
    "name": "Mackenzie SAR"
  },
  {
    "id": "9202836C-DC5C-4C62-8190-022A03769098",
    "org": "BCSARA",
    "name": "Revelstoke SAR"
  },
  {
    "id": "BE921E46-2521-4B8C-9438-0645CCB19DE8",
    "org": "BCSARA",
    "name": "Arrowsmith SAR"
  },
  {
    "id": "2F07BE02-EC9F-435D-B8E2-0B31799879BC",
    "org": "BCSARA",
    "name": "Quesnel SAR"
  },
  {
    "id": "C111498E-74F0-46B3-8442-0B38D435C854",
    "org": "BCSARA",
    "name": "Juan de Fuca SAR"
  },
  {
    "id": "16FAD27A-76E6-471E-A3FA-146CCB740DBC",
    "org": "BCSARA",
    "name": "Kent Harrison SAR"
  },
  {
    "id": "4A2BA222-3766-4F38-86E4-1724FDE94AF3",
    "org": "BCSARA",
    "name": "Logan Lake SAR"
  },
  {
    "id": "5C8A48A2-62F6-44E8-93CC-18ECAAE7E2ED",
    "org": "BCSARA",
    "name": "Arrow Lakes SAR"
  },
  {
    "id": "DBCE7252-92D1-481F-ADD0-1923F1F7FD39",
    "org": "BCSARA",
    "name": "Castlegar SAR"
  },
  {
    "id": "F2874DE5-0066-45A5-A3F8-1A38A64D67EC",
    "org": "BCSARA",
    "name": "Cowichan SAR"
  },
  {
    "id": "499A9B5C-E712-4968-8B9F-1DEB9D402915",
    "org": "BCSARA",
    "name": "Campbell River SAR"
  },
  {
    "id": "0EBB892E-F241-466A-B1E1-1E05F01EF0C7",
    "org": "BCSARA",
    "name": "North Shore SAR"
  },
  {
    "id": "52078C4B-4A25-4103-A7EA-224B68AB5C55",
    "org": "BCSARA",
    "name": "West Chilcotin SAR"
  },
  {
    "id": "BFDAB6B8-BEE2-4157-A144-23965C166BD8",
    "org": "BCSARA",
    "name": "Stewart SAR"
  },
  {
    "id": "E05BB4DE-8786-4289-B39B-2574C41E2777",
    "org": "BCSARA",
    "name": "Houston SAR"
  },
  {
    "id": "76A1101B-464D-4D12-ABBC-266599F2F5DD",
    "org": "BCSARA",
    "name": "Robson Valley SAR"
  },
  {
    "id": "D44C628D-E9AD-43CE-9671-2965C64FF0E5",
    "org": "BCSARA",
    "name": "Fernie SAR"
  },
  {
    "id": "F964C5E1-2337-4761-AB36-2965F57E7DC4",
    "org": "BCSARA",
    "name": "Atlin SAR"
  },
  {
    "id": "62231DA2-DCB8-413E-8C60-2A0B2E8DC214",
    "org": "BCSARA",
    "name": "Parkland SAR"
  },
  {
    "id": "37F43ECF-9CD5-4EB5-9699-2C0DBB7974F3",
    "org": "BCSARA",
    "name": "Ladysmith SAR"
  },
  {
    "id": "5B2C5A11-07DC-4104-99A5-364C204D4B32",
    "org": "BCSARA",
    "name": "Nicola Valley SAR"
  },
  {
    "id": "937148E6-72FD-456B-9DD9-38E975492D5F",
    "org": "BCSARA",
    "name": "Nanaimo SAR"
  },
  {
    "id": "124CA510-0BD2-4F53-82BE-3A5F4960BFCC",
    "org": "BCSARA",
    "name": "Penticton SAR"
  },
  {
    "id": "0B0DC8D4-9A62-4987-8EFA-43FC2A31D598",
    "org": "BCSARA",
    "name": "Whistler SAR"
  },
  {
    "id": "87756CEF-01AC-493A-89BE-464CADAE7EE1",
    "org": "BCSARA",
    "name": "Kimberley SAR"
  },
  {
    "id": "74E5E639-A831-427F-8494-4DCD0A55BF37",
    "org": "BCSARA",
    "name": "Creston Valley SAR"
  },
  {
    "id": "6A39C786-4C74-4B1E-91A6-4E1FCFE7584D",
    "org": "BCSARA",
    "name": "Kitimat SAR"
  },
  {
    "id": "7AF5AD55-2655-4218-B693-56F48353E190",
    "org": "BCSARA",
    "name": "South Columbia SAR"
  },
  {
    "id": "11A311E6-6768-46AA-9F3C-571AA95E3726",
    "org": "BCSARA",
    "name": "Nakusp SAR"
  },
  {
    "id": "65D6C93C-63F9-476F-8A63-5C8A968F4E11",
    "org": "BCSARA",
    "name": "PEMO SAR"
  },
  {
    "id": "D83B66D5-C697-448F-9E4F-5DA7828A66A5",
    "org": "BCSARA",
    "name": "Metchosin SAR"
  },
  {
    "id": "9893E045-D590-44E4-8AF4-5DBB1F1661A4",
    "org": "BCSARA",
    "name": "Prince Rupert SAR"
  },
  {
    "id": "B3AE6204-9E95-452A-9C10-5EB4178E0ABE",
    "org": "BCSARA",
    "name": "Pemberton SAR"
  },
  {
    "id": "2207EB6C-E292-47E8-AE3D-68855B846109",
    "org": "BCSARA",
    "name": "Powell River SAR"
  },
  {
    "id": "A1C1A217-4AE3-462C-A7D4-68FFAA8C0210",
    "org": "BCSARA",
    "name": "Rossland SAR"
  },
  {
    "id": "98851139-E736-4974-A672-6972F3A8965F",
    "org": "BCSARA",
    "name": "South Peace SAR"
  },
  {
    "id": "AB67B6D4-F795-43AD-9506-69880F7BEAFD",
    "org": "BCSARA",
    "name": "Alberni Valley Rescue Squad"
  },
  {
    "id": "8940A059-6A5A-4004-9D1E-758C4D576C2E",
    "org": "BCSARA",
    "name": "Bulkley Valley SAR"
  },
  {
    "id": "169C529D-792A-4615-ABE9-78203A6A70A4",
    "org": "BCSARA",
    "name": "Grand Forks SAR"
  },
  {
    "id": "88B20B0B-04BC-4596-A2F5-7CCCB317A4A0",
    "org": "BCSARA",
    "name": "Ridge Meadows SAR"
  },
  {
    "id": "FEC27732-35F1-43D6-9597-7E0D2FEEDD65",
    "org": "BCSARA",
    "name": "Mission SAR"
  },
  {
    "id": "CDA9B3A3-FC65-4803-8685-813BCE298DEF",
    "org": "BCSARA",
    "name": "Bella Coola Valley SAR"
  },
  {
    "id": "2EFA81F4-3E9B-4E45-BE94-8166AAA9298C",
    "org": "BCSARA",
    "name": "Keremeos SAR"
  },
  {
    "id": "FF7F03D5-E414-443F-8315-82BB378ABBD8",
    "org": "BCSARA",
    "name": "Comox Valley SAR"
  },
  {
    "id": "4643747E-FB2A-4230-B4B8-8506F9951DFF",
    "org": "BCSARA",
    "name": "Chetwynd SAR"
  },
  {
    "id": "B865EDF6-F0A7-4241-8CD4-8A5942C7B18A",
    "org": "BCSARA",
    "name": "Tumbler Ridge SAR"
  },
  {
    "id": "589F720D-A304-49CF-B40C-8E944D7C9D2F",
    "org": "BCSARA",
    "name": "Fort St. James SAR"
  },
  {
    "id": "893B590C-A159-4A89-9CA4-A3DF24D6ABFE",
    "org": "BCSARA",
    "name": "Sunshine Coast SAR"
  },
  {
    "id": "B04FE1E7-979F-40CC-892C-A74EEA295ECB",
    "org": "BCSARA",
    "name": "Kaslo SAR"
  },
  {
    "id": "8B8D2A86-91D6-4606-B2D7-A9EDF3C8EE35",
    "org": "BCSARA",
    "name": "Burns Lake SAR"
  },
  {
    "id": "8FB71ABC-4C5C-43A8-8E68-AA75DD2262EB",
    "org": "BCSARA",
    "name": "Vernon SAR"
  },
  {
    "id": "CE558295-B9E2-41A3-88F1-AE029EC1AE0D",
    "org": "BCSARA",
    "name": "Kamloops SAR"
  },
  {
    "id": "DF7FBC23-17F2-41AB-8DEB-AF00D27C5B7F",
    "org": "BCSARA",
    "name": "Oliver Osoyoos SAR"
  },
  {
    "id": "64B9D581-05FD-4D9B-ABFF-B24BFAFCEA2C",
    "org": "BCSARA",
    "name": "Lions Bay SAR"
  },
  {
    "id": "3CD654FA-8B48-4C75-BB75-B7834639990C",
    "org": "BCSARA",
    "name": "South Cariboo SAR"
  },
  {
    "id": "F7CD798B-52AD-423E-B66F-BD01D3B70D5D",
    "org": "BCSARA",
    "name": "Squamish SAR"
  },
  {
    "id": "D0AEC6BB-EE25-437B-8A8C-BEAA284FF685",
    "org": "BCSARA",
    "name": "Fort Nelson SAR"
  },
  {
    "id": "890789F2-9DB1-4785-BF00-BF051676B11E",
    "org": "BCSARA",
    "name": "Shuswap SAR"
  },
  {
    "id": "2679596A-3D96-4E74-913E-BF273235FC6F",
    "org": "BCSARA",
    "name": "Nechako Valley SAR"
  },
  {
    "id": "EA48BC49-A566-4248-A4B5-C1A6DBBEF00B",
    "org": "BCSARA",
    "name": "Central Fraser Valley SAR"
  },
  {
    "id": "12FDF8F5-4127-456E-9F6D-C6912161BE6F",
    "org": "BCSARA",
    "name": "Columbia Valley SAR"
  },
  {
    "id": "20A1A9F3-CB11-43F8-BEFE-C8933A566764",
    "org": "BCSARA",
    "name": "Prince George SAR"
  },
  {
    "id": "C704D0F8-AF89-4143-BD3E-CB4EAC7A7AA7",
    "org": "BCSARA",
    "name": "Central Okanagan SAR"
  },
  {
    "id": "EF91565B-77F8-428B-9D15-D0EAA4043A0E",
    "org": "BCSARA",
    "name": "Hope SAR"
  },
  {
    "id": "97717FBA-977C-49CD-B105-D55FA705AA14",
    "org": "BCSARA",
    "name": "North Peace SAR"
  },
  {
    "id": "83081A8A-6C30-45A8-B9B1-D625090148D6",
    "org": "BCSARA",
    "name": "Elkford SAR"
  },
  {
    "id": "6C4ED3C8-18D1-4F25-BEB1-D8C3B5272267",
    "org": "BCSARA",
    "name": "Coquitlam SAR"
  },
  {
    "id": "6FD79D61-ED33-46E1-A1AA-E3BC1F24A143",
    "org": "BCSARA",
    "name": "Chilliwack SAR"
  },
  {
    "id": "C0A7C62C-8C76-43F5-9357-E65394CCA2CB",
    "org": "BCSARA",
    "name": "South Fraser SAR"
  },
  {
    "id": "452E4432-F01C-4FDB-8DB4-E7399FC09A97",
    "org": "BCSARA",
    "name": "Sparwood SAR"
  },
  {
    "id": "0E63E227-27A8-4B11-8043-EC2C589A4CBA",
    "org": "BCSARA",
    "name": "Golden SAR"
  },
  {
    "id": "3642094A-274C-44DA-B379-ED42E9265FF8",
    "org": "BCSARA",
    "name": "Central Cariboo SAR"
  },
  {
    "id": "D5A57651-6C40-4A8E-A442-F0D7294FE0ED",
    "org": "BCSARA",
    "name": "Terrace SAR"
  },
  {
    "id": "8CA3E11B-5A87-4C72-A11C-F14225AC7AAF",
    "org": "BCSARA",
    "name": "Princeton SAR"
  },
  {
    "id": "77F87A03-46E8-4C70-A05B-F32DAE58276B",
    "org": "BCSARA",
    "name": "Westcoast Inland SAR"
  },
  {
    "id": "8E824695-1EDD-49FE-BADF-F42F8A34A95F",
    "org": "BCSARA",
    "name": "Salt Spring Island SAR"
  },
  {
    "id": "5153C373-4B73-45F6-99B6-F4DA00D28B92",
    "org": "BCSARA",
    "name": "Wells Gray SAR"
  },
  {
    "id": "B2CD40D5-6ABF-4FF8-A89E-F5FE6B995C89",
    "org": "BCSARA",
    "name": "Nelson SAR"
  },
  {
    "id": "71FFF997-108B-4DDF-914E-F81069F8EA26",
    "org": "BCSARA",
    "name": "Barriere SAR"
  },
  {
    "id": "A3190007-E0EA-49F8-95F8-F8FF8396A38B",
    "org": "BCSARA",
    "name": "Cranbrook SAR"
  },
  {
    "id": "F1B9CA16-CB19-4DD2-961F-FE3EB6CC6477",
    "org": "BCSARA",
    "name": "Archipelago SAR"
  },
  {
    "id": "A52F1CD3-CE79-4AA7-BEA4-EA5BCB4DBC3C",
    "org": "ABSAR",
    "name": "Alberta/British Columbia Cave Rescue"
  },
  {
    "id": "F18ACA88-3F15-4F94-A067-E0F7195331DE",
    "org": "ABSAR",
    "name": "Badlands Search and Rescue"
  },
  {
    "id": "FB594701-8FB9-49B1-AD06-9F0CE462A0B0",
    "org": "ABSAR",
    "name": "Bonnyville SAR"
  },
  {
    "id": "5AEA95A1-398A-4A9F-86DC-DAFFD1550E1C",
    "org": "ABSAR",
    "name": "Brazeau Regional Search and Rescue"
  },
  {
    "id": "2107B4FA-A818-4951-9E76-19E43FA78E10",
    "org": "ABSAR",
    "name": "Calgary Search and Rescue Association"
  },
  {
    "id": "EE92AA60-D987-483F-8CCB-A49A27EA251F",
    "org": "ABSAR",
    "name": "Calling Lake Search and Rescue"
  },
  {
    "id": "D00E558F-AABA-4C27-A791-88C55C3200AD",
    "org": "ABSAR",
    "name": "Canadian Search Dog Association"
  },
  {
    "id": "78CC6C91-48F2-4A8A-93B1-5B4C751FDAEE",
    "org": "ABSAR",
    "name": "Central Zone Search and Rescue"
  },
  {
    "id": "BE2C305E-A83F-411A-82FA-7CCC07E8C945",
    "org": "ABSAR",
    "name": "Cochrane Search and Rescue "
  },
  {
    "id": "1146DE80-75A9-431C-93FA-A50F2BE3D882",
    "org": "ABSAR",
    "name": "Cold Lake Search and Rescue"
  },
  {
    "id": "1CD64BE4-3BDB-471F-B433-2A3F5B65A426",
    "org": "ABSAR",
    "name": "Edmonton Regional SAR"
  },
  {
    "id": "52DE1A5C-5421-4BF3-B5A5-13F22825BDA0",
    "org": "ABSAR",
    "name": "Foothills Search & Rescue"
  },
  {
    "id": "C1307123-D412-4906-940D-5E8E7A65C7A2",
    "org": "ABSAR",
    "name": "Fort McMurray SAR"
  },
  {
    "id": "98632A6A-7984-46E9-9C20-21FD38F908CF",
    "org": "ABSAR",
    "name": "Grande Cache SAR"
  },
  {
    "id": "0920E8BD-F0C1-4314-B294-50689BB83ADF",
    "org": "ABSAR",
    "name": "Greenview Search and Rescue Association"
  },
  {
    "id": "55F762C4-594E-4716-A3A9-A7FA7C6F16D2",
    "org": "ABSAR",
    "name": "Hinton Search & Rescue"
  },
  {
    "id": "56DF7757-DD4E-4B03-B972-C0922ACA3272",
    "org": "ABSAR",
    "name": "Klondike Trail SAR"
  },
  {
    "id": "92D9089B-8B57-4BA1-A833-DA3389F97D39",
    "org": "ABSAR",
    "name": "LASARA"
  },
  {
    "id": "6F951735-6400-45AB-8D5B-470BEAF92397",
    "org": "ABSAR",
    "name": "Lesser Slave Lake Search and Rescue"
  },
  {
    "id": "02C80D21-6A55-4107-8180-AE263C77A2BA",
    "org": "ABSAR",
    "name": "Little Divide Search and Rescue"
  },
  {
    "id": "5BA2D51B-C5F5-4D06-BB3F-A809257F5FD7",
    "org": "ABSAR",
    "name": "Mountain View Search & Rescue"
  },
  {
    "id": "38F21B78-00BD-43D5-8422-9526CE6F929F",
    "org": "ABSAR",
    "name": "Parkland Search and Rescue"
  },
  {
    "id": "B25D8BB0-9CFE-41A9-88B9-E7DA8BBBA318",
    "org": "ABSAR",
    "name": "Peace Region Search and Rescue"
  },
  {
    "id": "21F36B99-445D-43F3-B7DA-843FC1B4A55C",
    "org": "ABSAR",
    "name": "Pincher Creek Search & Rescue"
  },
  {
    "id": "F333977A-3BF0-4780-80F5-69D070488AC0",
    "org": "ABSAR",
    "name": "Red Deer County SAR"
  },
  {
    "id": "83978072-06CB-45E2-8C22-61D6E93917DE",
    "org": "ABSAR",
    "name": "Rocky Mountain House Search & Rescue"
  },
  {
    "id": "EBAC4741-CBC7-47C3-A132-E396FC1174C6",
    "org": "ABSAR",
    "name": "SARDAA"
  },
  {
    "id": "E50F1F97-2E42-4CA9-8C26-704E0C23282A",
    "org": "ABSAR",
    "name": "South Eastern Alberta Search and Rescue"
  },
  {
    "id": "4F020A6A-5CF4-4479-A6AF-A6319DB3800F",
    "org": "ABSAR",
    "name": "St Paul SAR"
  },
  {
    "id": "7A5DCB28-0244-4DFF-98C1-5C6DAA46D7E8",
    "org": "ABSAR",
    "name": "Sundre Volunteer Search and Rescue"
  },
  {
    "id": "5347C261-0187-4044-8B58-ED494B1FF805",
    "org": "ABSAR",
    "name": "Technical Search and Rescue"
  },
  {
    "id": "19703F2D-4479-4D64-81E4-FA04B6144D87",
    "org": "ABSAR",
    "name": "Wetaskiwin Search and Rescue"
  },
  {
    "id": "E0E78144-CD98-4623-AB20-6020CBB68772",
    "org": "ABSAR",
    "name": "Whitecourt SAR"
  },
  {
    "id": "8a0165b4-71f2-4dc8-ac6f-09b9ea6678c3",
    "org": "Euro",
    "name": "SAR Team \u2013 Associa\u00e7\u00e3o de Volunt\u00e1rios de Prote\u00e7\u00e3o Civil, EVOLSAR"
  },
  {
    "id": "f01f53e3-fed4-4931-9c31-ebc1533a3f31",
    "org": "Euro",
    "name": "EFRU \u2013 Emergency Fire & Rescue Unit, EVOLSAR"
  },
  {
    "id": "9fda8fc9-6de5-4228-8129-b17145735535",
    "org": "Euro",
    "name": "SARAID \u2013 Search and Rescue Assistance in Disasters, EVOLSAR"
  },
  {
    "id": "07a93b03-9eba-48cb-8062-80a5e25be7a6",
    "org": "Euro",
    "name": "PUI \u2013 Pompiers de l\u2019Urgence Internationale, EVOLSAR"
  },
  {
    "id": "7e5fedef-91e5-48a7-ae54-425a679c4c40",
    "org": "Euro",
    "name": "UCRS Madrid \u2013 Unidad Canina de Rescagte y Salvamento de Madrid, EVOLSAR"
  },
  {
    "id": "efab4677-59d7-4e97-ad60-1a0a06e79fe2",
    "org": "Euro",
    "name": "CCPVC \u2013 Cyprus Civil Protection Volunteer Corps, EVOLSAR"
  },
  {
    "id": "c5246a2f-3b44-4dfb-b8fa-f5b939ab368e",
    "org": "Euro",
    "name": "Serve ON, EVOLSAR"
  },
  {
    "id": "c15b622f-6d61-4060-9e87-160c0e50a8fb",
    "org": "Euro",
    "name": "SRT \u2013 Serbian Rescue Team, EVOLSAR"
  },
  {
    "id": "1a8d91de-c4bb-428b-bdf7-a340066d1e29",
    "org": "Euro",
    "name": "OPVE \u2013 Central Buda Volunteer Civil Protection Association, EVOLSAR"
  },
  {
    "id": "d2e8440a-c01a-4972-a7e5-02a99d56a079",
    "org": "Euro",
    "name": "EPOMEA \u2013 Elite Team Special Mission of Greece, EVOLSAR"
  },
  {
    "id": "d6511edf-e552-4afc-a608-94d72e3815d5",
    "org": "Euro",
    "name": "Edelweiss, EVOLSAR"
  },
  {
    "id": "63f28253-d774-43c7-8164-90111895173c",
    "org": "Euro",
    "name": "AHBVP \u2013 Bombeiros Volunt\u00e1rios de Peniche, EVOLSAR"
  },
  {
    "id": "70bf8a7e-2d7a-4fd7-bf6a-eca938c2a29e",
    "org": "Euro",
    "name": "Rescue GR, EVOLSAR"
  },
  {
    "id": "9c31d966-89d8-4ed8-b23c-7b38e0b745e8",
    "org": "Euro",
    "name": "Angeli Della Sila, EVOLSAR"
  },
  {
    "id": "f0273de9-f7e5-4a95-9ca8-f20a75e5777f",
    "org": "Euro",
    "name": "Protezione Civile Antelao, EVOLSAR"
  },
  {
    "id": "8ebe34f2-09c2-45f5-abd7-2bed92409a4b",
    "org": "Euro",
    "name": "GIANNINO CARIA, EVOLSAR"
  },
  {
    "id": "4beb346f-abad-40f2-8f16-8a558e2a169c",
    "org": "Portugal",
    "name": "APMC \u2013 Associa\u00e7\u00e3o Portuguesa de Mantrailing e Canicross"
  },
  {
    "id": "de306c0e-f4d4-4b8c-a1f7-00c7b91687bb",
    "org": "Portugal",
    "name": "K9H CIOPS \u2013 Corpo de Interven\u00e7\u00e3o em Opera\u00e7\u00f5es Prote\u00e7\u00e3o e Socorro"
  },
  {
    "id": "f00487f3-6369-461b-b2b2-5a010084b291",
    "org": "Portugal",
    "name": "IRA \u2013 Interven\u00e7\u00e3o e Resgate Animal"
  },
  {
    "id": "375479b3-d36d-4983-be4d-0921dffa5c84",
    "org": "Portugal",
    "name": "UPIR \u2013 Unidade Portuguesa Interven\u00e7\u00e3o e Resgate"
  },
  {
    "id": "7d11a174-bba3-46d6-8e4e-b34c73a0500d",
    "org": "Portugal",
    "name": "ARC \u2013 Associa\u00e7\u00e3o de Resgate Cinot\u00e9cnico"
  },
  {
    "id": "f344c49c-945e-4cea-9518-8f3e2b0915ca",
    "org": "Portugal",
    "name": "APBS \u2013 Associa\u00e7\u00e3o Portuguesa de Busca e Salvamento"
  },
  {
    "id": "0c65dc19-3cc1-47b0-afac-9b48fa59ed3a",
    "org": "Portugal",
    "name": "GNR \u2013 Guarda Nacional Republicana"
  },
  {
    "id": "b6ee6f2b-7c85-4c7d-b7b0-72fb3ace0389",
    "org": "Portugal",
    "name": "UEPS \u2013 Unidade Emerg\u00eancia Prote\u00e7\u00e3o e Socorro"
  },
  {
    "id": "3df714ce-ccc5-426f-af57-fd987e1daafb",
    "org": "Portugal",
    "name": "UEPS PIPS \u2013 Pelot\u00e3o de Interven\u00e7\u00e3o Prote\u00e7\u00e3o e Socorro"
  },
  {
    "id": "77aa7eb5-fb34-4527-b274-fb105edb1854",
    "org": "Portugal",
    "name": "UEPS Montanha \u2013 Busca e Resgate em Montanha"
  },
  {
    "id": "43ca4c7d-2922-4aed-95be-b4a0b3472100",
    "org": "Portugal",
    "name": "GIC GNR \u2013 Grupo Interven\u00e7\u00e3o Cinot\u00e9cnico"
  },
  {
    "id": "736cce7f-abf7-43da-919f-caa272db7a99",
    "org": "Portugal",
    "name": "PSP \u2013 Policia Seguran\u00e7a P\u00fablica"
  },
  {
    "id": "0723314b-9eca-4c36-82a2-4040ac8bc53b",
    "org": "Portugal",
    "name": "PJ \u2013 Policia Judici\u00e1ria"
  },
  {
    "id": "698200df-5294-4592-b367-58084d1c408f",
    "org": "Portugal",
    "name": "FOE \u2013 For\u00e7a de Opera\u00e7\u00f5es Especiais"
  },
  {
    "id": "6c1a79ea-60f7-4c19-895d-65d966cb63fd",
    "org": "Portugal",
    "name": "CVP \u2013 Cruz Vermelha Portuguesa"
  },
  {
    "id": "294c6071-b790-45f0-bb48-46c0be473022",
    "org": "Portugal",
    "name": "ANEPC \u2013 Autoridade Nacional Emerg\u00eancia Prote\u00e7\u00e3o Civil"
  },
  {
    "id": "008d5f52-f165-4228-bac9-ce7575585e7f",
    "org": "Portugal",
    "name": "FEPC \u2013 For\u00e7a Especial de Prote\u00e7\u00e3o Civil"
  },
  {
    "id": "e5e24919-a592-481b-b8a8-0183aae32912",
    "org": "Portugal",
    "name": "Bombeiros Municipais de Loul\u00e9"
  },
  {
    "id": "4ac46014-643a-4fb8-90ad-d518646b07e5",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Portim\u00e3o"
  },
  {
    "id": "22eaa153-cf3e-49f8-ae5e-0b484edf6b3a",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Albufeira"
  },
  {
    "id": "0c0de226-2a95-4fb1-a85a-840df88b4c78",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Lagos"
  },
  {
    "id": "03eee73b-bb46-4a81-a11b-8dd7dc72e461",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Vila do Bispo"
  },
  {
    "id": "2c0b8f40-8a08-4e25-b5fd-6a6e96b3bd50",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Aljezur"
  },
  {
    "id": "48ea93ef-a533-4290-9b10-e38a5693e1d8",
    "org": "Portugal",
    "name": "GSE \u2013 Grupo de Salvamentos Especiais"
  },
  {
    "id": "bae439fa-da7f-4774-bcb0-2d5739a0239e",
    "org": "Portugal",
    "name": "Bombeiros Mistos de Amora"
  },
  {
    "id": "9a567b9b-4f5f-490f-b3da-9bbb1e8c6bfc",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Cacilhas"
  },
  {
    "id": "cb5fb786-5b89-4eed-b276-8d7d453d6ead",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Mora"
  },
  {
    "id": "fa7775e9-8bdd-4a30-a875-39024a90396d",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Minde"
  },
  {
    "id": "a2555425-b67b-458c-8e6d-2ed7419cef8a",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Aveiro Velhos"
  },
  {
    "id": "4a0614fb-798f-4081-ab32-28ff7297987a",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Oliveira do Bairro"
  },
  {
    "id": "1020c293-5b90-4759-bb46-4aa93bb38c30",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de P\u00f3voa de Lanhoso"
  },
  {
    "id": "eedaa4a4-6f41-4cec-b0ab-4c91aa3c2912",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Bai\u00e3o"
  },
  {
    "id": "0c5876c6-5844-4555-8476-4086836bfd1c",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Santa Marinha do Z\u00eazere"
  },
  {
    "id": "6601abe5-0d98-4bca-bb25-2f6a85effd6e",
    "org": "Portugal",
    "name": "Bombeiros Volunt\u00e1rios de Viseu"
  },
  {
    "id": "b7e94356-f43b-4adc-95aa-7d429a341879",
    "org": "Portugal",
    "name": "Bombeiros Sapadores do Porto"
  },
  {
    "id": "86482a7f-0ffb-4e60-ad90-77b875157400",
    "org": "Portugal",
    "name": "Bombeiros Sapadores de Lisboa"
  },
  {
    "id": "ce87c046-34cc-4812-9e51-58bc2332393c",
    "org": "Portugal",
    "name": "Bombeiros Sapadores do Cartaxo"
  },
  {
    "id": "a0d61ba8-1d0d-4dbd-a7fd-1a4ecb91a5ea",
    "org": "Portugal",
    "name": "Bombeiros do Concelho de Espinho"
  },
  {
    "id": "1C8C2043-4A7A-43D9-B035-21C5444816F8",
    "org": "SARVAC",
    "name": "SARVAC"
  },
  {
    "id": "5F48C5BD-6645-4920-A065-EDC67D7ABDE2",
    "org": "SARVAC",
    "name": "Humanitarian Workforce"
  },
  {
    "id": "cad7191c-df37-4ca6-bc6c-0ec19b9c957b",
    "org": "SARVAC",
    "name": "SAR Manitoba"
  },
  {
    "id": "af4df48e-9f82-45bb-b302-6b14b539e336",
    "org": "SARVAC",
    "name": "SAR New Brunswick"
  },
  {
    "id": "189e80f9-d552-4763-84f4-8bc3ac6c0af8",
    "org": "SARVAC",
    "name": "SAR Newfoundland and Labrador"
  },
  {
    "id": "7c4d74f3-d2aa-4569-93a1-845bdb179cb7",
    "org": "SARVAC",
    "name": "SAR Northwest Territories"
  },
  {
    "id": "EA620563-7DBF-4D20-88F9-BDB0A80C2C94",
    "org": "SARVAC",
    "name": "SAR Nova Scotia"
  },
  {
    "id": "96f19e34-5a42-445d-a935-40bc78162705",
    "org": "SARVAC",
    "name": "SAR Nunavut"
  },
  {
    "id": "871323c6-903d-4734-a2f8-a58613ab7996",
    "org": "SARVAC",
    "name": "SAR Ontario"
  },
  {
    "id": "907dbebe-270b-443e-8366-b5d368fa5335",
    "org": "SARVAC",
    "name": "SAR Prince Edward Island"
  },
  {
    "id": "6f0febc9-6740-4540-b42a-450f1a22a7ac",
    "org": "SARVAC",
    "name": "SAR Quebec"
  },
  {
    "id": "b6c70fac-07d9-4f8a-bb66-22c815001032",
    "org": "SARVAC",
    "name": "SAR Saskatchewan"
  },
  {
    "id": "a72a71ce-4f34-4e46-80a2-b2e524f8af64",
    "org": "SARVAC",
    "name": "SAR Yukon"
  },
  {
    "id": "65ec02d8-67a9-4ef9-83a4-8605e12fc88c",
    "org": "NCSAR",
    "name": "Cowee Search and Rescue"
  },
  {
    "id": "adf93714-a7f9-4cf1-b91e-ffb7030b5eda",
    "org": "NCSAR",
    "name": "NC Volunteer SAR"
  },
  {
    "id": "0ed3afc3-212d-4220-bb46-28a073359635",
    "org": "GA",
    "name": "White County SAR"
  },
  {
    "id": "05d07f03-1660-4e69-94d5-51a91bb2af87",
    "org": "GA",
    "name": "Friends of SAR, inc."
  },
  {
    "id": "93729cf8-f53c-4efc-a2c1-654bd11e9288",
    "org": "GA",
    "name": "Stephens County SAR"
  },
  {
    "id": "80c5650d-f91c-49e9-8f0c-382c159f7906",
    "org": "GA",
    "name": "Rabun County SAR"
  },
  {
    "id": "77c041c9-fa15-498c-837c-820a35188b01",
    "org": "GA",
    "name": "Union County SAR"
  },
  {
    "id": "d803f83b-da53-492e-a27a-e5a7a1233839",
    "org": "GA",
    "name": "Habersham County"
  },
  {
    "id": "2183b6ea-0267-40ec-8572-7ab844cb58e9",
    "org": "GA",
    "name": "Lumpkin County"
  },
  {
    "id": "54cdeae4-940c-489a-920c-b70bd46015f4",
    "org": "GA",
    "name": "Franklin County"
  },
  {
    "id": "5bf6f806-f11f-48df-b1e5-0fbdd99a5476",
    "org": "NBSAR",
    "name": "North West GSAR"
  },
  {
    "id": "9dcf452c-22af-44c3-aa32-30e61d8f743e",
    "org": "NBSAR",
    "name": "Acadie-Chaleur GSAR"
  },
  {
    "id": "14a38990-6e53-4982-b64c-846fe10b4420",
    "org": "NBSAR",
    "name": "Miramichi GSAR"
  },
  {
    "id": "8ed9f2e6-cd21-49fd-898e-3b10abb5a0d0",
    "org": "NBSAR",
    "name": "Tri-County GSAR"
  },
  {
    "id": "3871123d-3678-4b7c-ace0-b6bf19275b0d",
    "org": "NBSAR",
    "name": "Greater Fundy GSAR"
  },
  {
    "id": "863fc64b-db75-4198-a79f-c80031bc5fd4",
    "org": "NBSAR",
    "name": "River Valley GSAR"
  },
  {
    "id": "597778cb-627d-4175-be26-65adb30dee8c",
    "org": "NBSAR",
    "name": "Charlotte County GSAR"
  },
  {
    "id": "a8ccf5f1-4b2d-48b5-bc04-d48d2f9744c8",
    "org": "NBSAR",
    "name": "York Sunbury SAR"
  },
  {
    "id": "bcbe0646-6e04-4e58-97fb-e9ec3708e228",
    "org": "NBSAR",
    "name": "Carleton GSAR"
  },
  {
    "id": "6b7e460d-2490-4a8c-b828-5c1d7d707c83",
    "org": "LE",
    "name": "Ontario Prov. Police"
  },
  {
    "id": "75467ef9-fee0-4911-b54f-62e1ba926095",
    "org": "LE",
    "name": "Police"
  },
  {
    "id": "85755fe3-d757-4bdc-87c2-156ccafbdc57",
    "org": "LE",
    "name": "Royal Canadian Mounted Police"
  },
  {
    "id": "c0376477-71c3-42ba-bcba-4d674dd18572",
    "org": "LE",
    "name": "Sheriff"
  },
  {
    "id": "489f9815-808d-4f55-a17f-214d352e7661",
    "org": "BCSARA",
    "name": "BC Search Dog Association"
  },
  {
    "id": "008bdd33-28a1-46b6-818d-59225f2e97df",
    "org": "BCSARA",
    "name": "BC Tracking Association"
  },
  {
    "id": "88A344BD-BEED-4727-A353-3E75B028507D",
    "org": "BCSARA",
    "name": "Critical Incident Stress Management"
  },
  {
    "id": "d7d6350e-7666-4ef1-9205-f38edd1efc1f",
    "org": "OtherOrgs",
    "name": "Convergent Volunteer"
  },
  {
    "id": "b98654a4-2e95-4d20-b8c3-80a0cf565075",
    "org": "OtherOrgs",
    "name": "Community Volunteer"
  },
  {
    "id": "2c4ff368-fe8b-41d9-a34d-7c2691b73138",
    "org": "OtherOrgs",
    "name": "First Nations Member"
  },
  {
    "id": "8CBE0C6D-78B1-4600-96C0-21E3C16A444D",
    "org": "OtherOrgs",
    "name": "Great Hat Web Design"
  },
  {
    "id": "02035C34-CD9C-4B3D-9C22-5AF29068A0D9",
    "org": "OtherOrgs",
    "name": "Non-SAR"
  },
  {
    "id": "96BA69A4-436C-4DA1-85B1-992E84C36019",
    "org": "OtherOrgs",
    "name": "Unassigned"
  }
]
