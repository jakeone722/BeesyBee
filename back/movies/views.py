from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import json
import pandas as pd
from .models import Moviedata, Movie, Review
import requests
import random 
from django.http import JsonResponse
from .serializers import MovieSerializer, ReviewSerializer
from accounts.models import User
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

MOVIE_FEMALE = [{'movie_id': 745, 'movie_rate_avg': 4.644444444444445, 'movie_rate_total': 836, 'movie_count': 180}, {'movie_id': 1148, 'movie_rate_avg': 4.588235294117647, 'movie_rate_total': 1092, 'movie_count': 
238}, {'movie_id': 922, 'movie_rate_avg': 4.572649572649572, 'movie_rate_total': 535, 'movie_count': 117}, {'movie_id': 527, 'movie_rate_avg': 4.56260162601626, 'movie_rate_total': 2806, 'movie_count': 615}, {'movie_id': 318, 'movie_rate_avg': 4.539074960127592, 'movie_rate_total': 2846, 'movie_count': 627}, {'movie_id': 1223, 'movie_rate_avg': 4.537878787878788, 'movie_rate_total': 599, 'movie_count': 132}, {'movie_id': 1207, 'movie_rate_avg': 4.536666666666667, 'movie_rate_total': 1361, 'movie_count': 300}, {'movie_id': 3429, 'movie_rate_avg': 4.513888888888889, 'movie_rate_total': 325, 'movie_count': 72}, {'movie_id': 50, 'movie_rate_avg': 4.513317191283293, 'movie_rate_total': 1864, 'movie_count': 413}, {'movie_id': 905, 'movie_rate_avg': 4.5, 'movie_rate_total': 585, 'movie_count': 130}, {'movie_id': 904, 'movie_rate_avg': 4.484536082474227, 'movie_rate_total': 1305, 'movie_count': 291}, {'movie_id': 2019, 'movie_rate_avg': 4.481132075471698, 'movie_rate_total': 475, 'movie_count': 106}, {'movie_id': 2762, 'movie_rate_avg': 4.477409638554217, 'movie_rate_total': 2973, 'movie_count': 664}, {'movie_id': 1212, 'movie_rate_avg': 4.466019417475728, 'movie_rate_total': 460, 'movie_count': 103}, {'movie_id': 910, 'movie_rate_avg': 4.462745098039216, 'movie_rate_total': 1138, 'movie_count': 255}, {'movie_id': 3307, 'movie_rate_avg': 4.4520547945205475, 'movie_rate_total': 325, 'movie_count': 73}, {'movie_id': 930, 'movie_rate_avg': 4.448717948717949, 'movie_rate_total': 694, 'movie_count': 156}, {'movie_id': 898, 'movie_rate_avg': 4.446808510638298, 'movie_rate_total': 1045, 'movie_count': 235}, {'movie_id': 2324, 'movie_rate_avg': 4.422343324250681, 'movie_rate_total': 1623, 'movie_count': 367}]


MOVIE_MALE = [{'movie_id': 858, 'movie_rate_avg': 4.583333333333333, 'movie_rate_total': 7975, 'movie_count': 1740}, {'movie_id': 2019, 'movie_rate_avg': 4.576628352490421, 'movie_rate_total': 2389, 'movie_count': 522}, {'movie_id': 318, 'movie_rate_avg': 4.560625, 'movie_rate_total': 7297, 'movie_count': 1600}, {'movie_id': 1198, 'movie_rate_avg': 4.520597322348094, 'movie_rate_total': 8779, 'movie_count': 1942}, {'movie_id': 50, 'movie_rate_avg': 4.518248175182482, 'movie_rate_total': 6190, 'movie_count': 1370}, {'movie_id': 260, 'movie_rate_avg': 4.495307167235495, 'movie_rate_total': 10537, 'movie_count': 2344}, {'movie_id': 527, 'movie_rate_avg': 4.49141503848431, 'movie_rate_total': 7586, 'movie_count': 1689}, {'movie_id': 1148, 'movie_rate_avg': 4.478260869565218, 'movie_rate_total': 2884, 'movie_count': 644}, {'movie_id': 745, 'movie_rate_avg': 4.473794549266247, 'movie_rate_total': 2134, 'movie_count': 477}, {'movie_id': 904, 'movie_rate_avg': 4.4729907773386035, 'movie_rate_total': 3395, 'movie_count': 759}, {'movie_id': 3435, 'movie_rate_avg': 4.468354430379747, 'movie_rate_total': 1765, 'movie_count': 395}, {'movie_id': 750, 'movie_rate_avg': 4.464788732394366, 'movie_rate_total': 5072, 'movie_count': 1136}, {'movie_id': 922, 
'movie_rate_avg': 4.4645892351274785, 'movie_rate_total': 1576, 'movie_count': 353}, {'movie_id': 912, 'movie_rate_avg': 4.461340206185567, 'movie_rate_total': 5193, 
'movie_count': 1164}, {'movie_id': 1212, 'movie_rate_avg': 4.448275862068965, 'movie_rate_total': 1677, 'movie_count': 377}, {'movie_id': 1204, 'movie_rate_avg': 4.439821693907875, 'movie_rate_total': 2988, 'movie_count': 673}, {'movie_id': 1221, 'movie_rate_avg': 4.437777777777778, 'movie_rate_total': 5991, 'movie_count': 1350}, 
{'movie_id': 1193, 'movie_rate_avg': 4.418423106947697, 'movie_rate_total': 5660, 'movie_count': 1281}, {'movie_id': 913, 'movie_rate_avg': 4.410891089108911, 'movie_rate_total': 3564, 'movie_count': 808}, {'movie_id': 1262, 'movie_rate_avg': 4.408940397350993, 'movie_rate_total': 2663, 'movie_count': 604}]

MOVIE_OCP_00 = [
  {
    "movie_id": 922,
    "movie_rate_avg": 4.6716417910447765,
    "movie_rate_total": 313,
    "movie_count": 67
  },
  {
    "movie_id": 1260,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 184,
    "movie_count": 40
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 256,
    "movie_count": 56
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.528735632183908,
    "movie_rate_total": 394,
    "movie_count": 87
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.525,
    "movie_rate_total": 362,
    "movie_count": 80
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.498054474708171,
    "movie_rate_total": 1156,
    "movie_count": 257
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.485714285714286,
    "movie_rate_total": 314,
    "movie_count": 70
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.48015873015873,
    "movie_rate_total": 1129,
    "movie_count": 252
  },
  {
    "movie_id": 950,
    "movie_rate_avg": 4.478260869565218,
    "movie_rate_total": 206,
    "movie_count": 46
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.472477064220183,
    "movie_rate_total": 975,
    "movie_count": 218
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.456310679611651,
    "movie_rate_total": 459,
    "movie_count": 103
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.447530864197531,
    "movie_rate_total": 1441,
    "movie_count": 324
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.446494464944649,
    "movie_rate_total": 1205,
    "movie_count": 271
  },
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.446153846153846,
    "movie_rate_total": 289,
    "movie_count": 65
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.435114503816794,
    "movie_rate_total": 581,
    "movie_count": 131
  },
  {
    "movie_id": 913,
    "movie_rate_avg": 4.430894308943089,
    "movie_rate_total": 545,
    "movie_count": 123
  },
  {
    "movie_id": 953,
    "movie_rate_avg": 4.425531914893617,
    "movie_rate_total": 416,
    "movie_count": 94
  },
  {
    "movie_id": 1147,
    "movie_rate_avg": 4.4186046511627906,
    "movie_rate_total": 190,
    "movie_count": 43
  }
]

MOVIE_OCP_01 = [
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.64935064935065,
    "movie_rate_total": 358,
    "movie_count": 77
  },
  {
    "movie_id": 913,
    "movie_rate_avg": 4.608695652173913,
    "movie_rate_total": 530,
    "movie_count": 115
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.561643835616438,
    "movie_rate_total": 666,
    "movie_count": 146
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.5610859728506785,
    "movie_rate_total": 1008,
    "movie_count": 221
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.535211267605634,
    "movie_rate_total": 322,
    "movie_count": 71
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.522123893805309,
    "movie_rate_total": 511,
    "movie_count": 113
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.518518518518518,
    "movie_rate_total": 244,
    "movie_count": 54
  },
  {
    "movie_id": 3030,
    "movie_rate_avg": 4.517241379310345,
    "movie_rate_total": 131,
    "movie_count": 29
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.469767441860465,
    "movie_rate_total": 961,
    "movie_count": 215
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.465753424657534,
    "movie_rate_total": 652,
    "movie_count": 146
  },
  {
    "movie_id": 3089,
    "movie_rate_avg": 4.464285714285714,
    "movie_rate_total": 125,
    "movie_count": 28
  },
  {
    "movie_id": 908,
    "movie_rate_avg": 4.448484848484848,
    "movie_rate_total": 734,
    "movie_count": 165
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.4471544715447155,
    "movie_rate_total": 547,
    "movie_count": 123
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.436781609195402,
    "movie_rate_total": 386,
    "movie_count": 87
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.426136363636363,
    "movie_rate_total": 779,
    "movie_count": 176
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.425837320574162,
    "movie_rate_total": 925,
    "movie_count": 209
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.425,
    "movie_rate_total": 885,
    "movie_count": 200
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.423469387755102,
    "movie_rate_total": 867,
    "movie_count": 196
  },
  {
    "movie_id": 922,
    "movie_rate_avg": 4.410714285714286,
    "movie_rate_total": 247,
    "movie_count": 56
  }
]

MOVIE_OCP_02 = [
  {
    "movie_id": 1267,
    "movie_rate_avg": 4.7272727272727275,
    "movie_rate_total": 156,
    "movie_count": 33
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.722222222222222,
    "movie_rate_total": 170,
    "movie_count": 36
  },
  {
    "movie_id": 1147,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 74,
    "movie_count": 16
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.618181818181818,
    "movie_rate_total": 254,
    "movie_count": 55
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.611111111111111,
    "movie_rate_total": 166,
    "movie_count": 36
  },
  {
    "movie_id": 1280,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 69,
    "movie_count": 15
  },
  {
    "movie_id": 1251,
    "movie_rate_avg": 4.588235294117647,
    "movie_rate_total": 78,
    "movie_count": 17
  },
  {
    "movie_id": 922,
    "movie_rate_avg": 4.575757575757576,
    "movie_rate_total": 151,
    "movie_count": 33
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.5588235294117645,
    "movie_rate_total": 155,
    "movie_count": 34
  },
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 164,
    "movie_count": 36
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.551724137931035,
    "movie_rate_total": 132,
    "movie_count": 29
  },
  {
    "movie_id": 3429,
    "movie_rate_avg": 4.523809523809524,
    "movie_rate_total": 95,
    "movie_count": 21
  },
  {
    "movie_id": 3730,
    "movie_rate_avg": 4.517241379310345,
    "movie_rate_total": 131,
    "movie_count": 29
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.517241379310345,
    "movie_rate_total": 262,
    "movie_count": 58
  },
  {
    "movie_id": 1225,
    "movie_rate_avg": 4.512820512820513,
    "movie_rate_total": 352,
    "movie_count": 78
  },
  {
    "movie_id": 903,
    "movie_rate_avg": 4.51063829787234,
    "movie_rate_total": 212,
    "movie_count": 47
  },
  {
    "movie_id": 919,
    "movie_rate_avg": 4.510204081632653,
    "movie_rate_total": 442,
    "movie_count": 98
  },
  {
    "movie_id": 908,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 297,
    "movie_count": 66
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 459,
    "movie_count": 102
  },
  {
    "movie_id": 1284,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 108,
    "movie_count": 24
  }
]

MOVIE_OCP_03 = [
  {
    "movie_id": 904,
    "movie_rate_avg": 4.725,
    "movie_rate_total": 189,
    "movie_count": 40
  },
  {
    "movie_id": 913,
    "movie_rate_avg": 4.636363636363637,
    "movie_rate_total": 204,
    "movie_count": 44
  },
  {
    "movie_id": 945,
    "movie_rate_avg": 4.615384615384615,
    "movie_rate_total": 60,
    "movie_count": 13
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.613333333333333,
    "movie_rate_total": 346,
    "movie_count": 75
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.612903225806452,
    "movie_rate_total": 286,
    "movie_count": 62
  },
  {
    "movie_id": 2329,
    "movie_rate_avg": 4.611111111111111,
    "movie_rate_total": 83,
    "movie_count": 18
  },
  {
    "movie_id": 899,
    "movie_rate_avg": 4.606060606060606,
    "movie_rate_total": 152,
    "movie_count": 33
  },
  {
    "movie_id": 950,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 69,
    "movie_count": 15
  },
  {
    "movie_id": 3548,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 55,
    "movie_count": 12
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 160,
    "movie_count": 35
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 64,
    "movie_count": 14
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 96,
    "movie_count": 21
  },
  {
    "movie_id": 942,
    "movie_rate_avg": 4.5625,
    "movie_rate_total": 73,
    "movie_count": 16
  },
  {
    "movie_id": 1276,
    "movie_rate_avg": 4.56,
    "movie_rate_total": 114,
    "movie_count": 25
  },
  {
    "movie_id": 909,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 82,
    "movie_count": 18
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.538461538461538,
    "movie_rate_total": 236,
    "movie_count": 52
  },
  {
    "movie_id": 898,
    "movie_rate_avg": 4.521739130434782,
    "movie_rate_total": 104,
    "movie_count": 23
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.517241379310345,
    "movie_rate_total": 262,
    "movie_count": 58
  },
  {
    "movie_id": 778,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 90,
    "movie_count": 20
  }
]

MOVIE_OCP_04 = [
  {
    "movie_id": 318,
    "movie_rate_avg": 4.683582089552239,
    "movie_rate_total": 1569,
    "movie_count": 335
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.649122807017544,
    "movie_rate_total": 1325,
    "movie_count": 285
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.595505617977528,
    "movie_rate_total": 409,
    "movie_count": 89
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.556363636363637,
    "movie_rate_total": 1253,
    "movie_count": 275
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.512195121951219,
    "movie_rate_total": 555,
    "movie_count": 123
  },
  {
    "movie_id": 1193,
    "movie_rate_avg": 4.495,
    "movie_rate_total": 899,
    "movie_count": 200
  },
  {
    "movie_id": 908,
    "movie_rate_avg": 4.4774774774774775,
    "movie_rate_total": 497,
    "movie_count": 111
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.474025974025974,
    "movie_rate_total": 689,
    "movie_count": 154
  },
  {
    "movie_id": 2324,
    "movie_rate_avg": 4.473404255319149,
    "movie_rate_total": 841,
    "movie_count": 188
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.465116279069767,
    "movie_rate_total": 384,
    "movie_count": 86
  },
  {
    "movie_id": 2858,
    "movie_rate_avg": 4.464354527938343,
    "movie_rate_total": 2317,
    "movie_count": 519
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.4575,
    "movie_rate_total": 1783,
    "movie_count": 400
  },
  {
    "movie_id": 306,
    "movie_rate_avg": 4.4523809523809526,
    "movie_rate_total": 187,
    "movie_count": 42
  },
  {
    "movie_id": 2571,
    "movie_rate_avg": 4.451127819548872,
    "movie_rate_total": 1776,
    "movie_count": 399
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.450151057401813,
    "movie_rate_total": 1473,
    "movie_count": 331
  },
  {
    "movie_id": 1945,
    "movie_rate_avg": 4.446808510638298,
    "movie_rate_total": 209,
    "movie_count": 47
  },
  {
    "movie_id": 1228,
    "movie_rate_avg": 4.444444444444445,
    "movie_rate_total": 360,
    "movie_count": 81
  },
  {
    "movie_id": 1213,
    "movie_rate_avg": 4.442922374429224,
    "movie_rate_total": 973,
    "movie_count": 219
  },
  {
    "movie_id": 1221,
    "movie_rate_avg": 4.442105263157894,
    "movie_rate_total": 844,
    "movie_count": 190
  },
  {
    "movie_id": 1172,
    "movie_rate_avg": 4.440677966101695,
    "movie_rate_total": 262,
    "movie_count": 59
  }
]

MOVIE_OCP_05 = [
  {
    "movie_id": 903,
    "movie_rate_avg": 4.714285714285714,
    "movie_rate_total": 66,
    "movie_count": 14
  },
  {
    "movie_id": 910,
    "movie_rate_avg": 4.6923076923076925,
    "movie_rate_total": 61,
    "movie_count": 13
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.679245283018868,
    "movie_rate_total": 248,
    "movie_count": 53
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.642857142857143,
    "movie_rate_total": 65,
    "movie_count": 14
  },
  {
    "movie_id": 3504,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 37,
    "movie_count": 8
  },
  {
    "movie_id": 922,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 37,
    "movie_count": 8
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.611111111111111,
    "movie_rate_total": 166,
    "movie_count": 36
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.595238095238095,
    "movie_rate_total": 193,
    "movie_count": 42
  },
  {
    "movie_id": 1221,
    "movie_rate_avg": 4.580645161290323,
    "movie_rate_total": 142,
    "movie_count": 31
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.578947368421052,
    "movie_rate_total": 174,
    "movie_count": 38
  },
  {
    "movie_id": 1193,
    "movie_rate_avg": 4.545454545454546,
    "movie_rate_total": 150,
    "movie_count": 33
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.538461538461538,
    "movie_rate_total": 59,
    "movie_count": 13
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.533333333333333,
    "movie_rate_total": 68,
    "movie_count": 15
  },
  {
    "movie_id": 2329,
    "movie_rate_avg": 4.529411764705882,
    "movie_rate_total": 77,
    "movie_count": 17
  },
  {
    "movie_id": 1213,
    "movie_rate_avg": 4.516129032258065,
    "movie_rate_total": 140,
    "movie_count": 31
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.512195121951219,
    "movie_rate_total": 185,
    "movie_count": 41
  },
  {
    "movie_id": 593,
    "movie_rate_avg": 4.511627906976744,
    "movie_rate_total": 194,
    "movie_count": 43
  },
  {
    "movie_id": 1704,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 90,
    "movie_count": 20
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.490566037735849,
    "movie_rate_total": 238,
    "movie_count": 53
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.483870967741935,
    "movie_rate_total": 278,
    "movie_count": 62
  }
]

MOVIE_OCP_06 = [
  {
    "movie_id": 318,
    "movie_rate_avg": 4.711340206185567,
    "movie_rate_total": 457,
    "movie_count": 97
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.705263157894737,
    "movie_rate_total": 447,
    "movie_count": 95
  },
  {
    "movie_id": 1224,
    "movie_rate_avg": 4.6923076923076925,
    "movie_rate_total": 61,
    "movie_count": 13
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.690476190476191,
    "movie_rate_total": 197,
    "movie_count": 42
  },
  {
    "movie_id": 1233,
    "movie_rate_avg": 4.617647058823529,
    "movie_rate_total": 157,
    "movie_count": 34
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.6063829787234045,
    "movie_rate_total": 433,
    "movie_count": 94
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.6022727272727275,
    "movie_rate_total": 405,
    "movie_count": 88
  },
  {
    "movie_id": 1238,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 69,
    "movie_count": 15
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.595238095238095,
    "movie_rate_total": 193,
    "movie_count": 42
  },
  {
    "movie_id": 3783,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 55,
    "movie_count": 12
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 55,
    "movie_count": 12
  },
  {
    "movie_id": 1132,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 55,
    "movie_count": 12
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.5754716981132075,
    "movie_rate_total": 485,
    "movie_count": 106
  },
  {
    "movie_id": 2336,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 192,
    "movie_count": 42
  },
  {
    "movie_id": 1252,
    "movie_rate_avg": 4.565217391304348,
    "movie_rate_total": 210,
    "movie_count": 46
  },
  {
    "movie_id": 2390,
    "movie_rate_avg": 4.533333333333333,
    "movie_rate_total": 68,
    "movie_count": 15
  },
  {
    "movie_id": 2028,
    "movie_rate_avg": 4.53,
    "movie_rate_total": 453,
    "movie_count": 100
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.52,
    "movie_rate_total": 113,
    "movie_count": 25
  },
  {
    "movie_id": 1203,
    "movie_rate_avg": 4.516129032258065,
    "movie_rate_total": 140,
    "movie_count": 31
  },
  {
    "movie_id": 1193,
    "movie_rate_avg": 4.513888888888889,
    "movie_rate_total": 325,
    "movie_count": 72
  }
]

MOVIE_OCP_07 = [
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.677966101694915,
    "movie_rate_total": 276,
    "movie_count": 59
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.607913669064748,
    "movie_rate_total": 1281,
    "movie_count": 278
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.576419213973799,
    "movie_rate_total": 1048,
    "movie_count": 229
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.542857142857143,
    "movie_rate_total": 318,
    "movie_count": 70
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.539267015706806,
    "movie_rate_total": 867,
    "movie_count": 191
  },
  {
    "movie_id": 678,
    "movie_rate_avg": 4.512820512820513,
    "movie_rate_total": 176,
    "movie_count": 39
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.507751937984496,
    "movie_rate_total": 1163,
    "movie_count": 258
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.490259740259741,
    "movie_rate_total": 1383,
    "movie_count": 308
  },
  {
    "movie_id": 1178,
    "movie_rate_avg": 4.470588235294118,
    "movie_rate_total": 152,
    "movie_count": 34
  },
  {
    "movie_id": 953,
    "movie_rate_avg": 4.464788732394366,
    "movie_rate_total": 317,
    "movie_count": 71
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.46041055718475,
    "movie_rate_total": 1521,
    "movie_count": 341
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.456521739130435,
    "movie_rate_total": 410,
    "movie_count": 92
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.431372549019608,
    "movie_rate_total": 452,
    "movie_count": 102
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.427083333333333,
    "movie_rate_total": 850,
    "movie_count": 192
  },
  {
    "movie_id": 2028,
    "movie_rate_avg": 4.4183006535947715,
    "movie_rate_total": 1352,
    "movie_count": 306
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.416666666666667,
    "movie_rate_total": 477,
    "movie_count": 108
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.414342629482071,
    "movie_rate_total": 1108,
    "movie_count": 251
  },
  {
    "movie_id": 593,
    "movie_rate_avg": 4.409090909090909,
    "movie_rate_total": 1261,
    "movie_count": 286
  },
  {
    "movie_id": 1172,
    "movie_rate_avg": 4.408450704225352,
    "movie_rate_total": 313,
    "movie_count": 71
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.407407407407407,
    "movie_rate_total": 476,
    "movie_count": 108
  }
]

MOVIE_OCP_08 = [
  {
    "movie_id": 1257,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 15,
    "movie_count": 3
  },
  {
    "movie_id": 3471,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 10,
    "movie_count": 2
  },
  {
    "movie_id": 1214,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 15,
    "movie_count": 3
  },
  {
    "movie_id": 728,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 3000,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1260,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1263,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 2068,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1411,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 741,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1278,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1425,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1280,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1295,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 908,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 1449,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  },
  {
    "movie_id": 2253,
    "movie_rate_avg": 5,
    "movie_rate_total": 5,
    "movie_count": 1
  }
]

MOVIE_OCP_09 = [
  {
    "movie_id": 1148,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 45,
    "movie_count": 9
  },
  {
    "movie_id": 1223,
    "movie_rate_avg": 4.833333333333333,
    "movie_rate_total": 29,
    "movie_count": 6
  },
  {
    "movie_id": 293,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.75,
    "movie_rate_total": 38,
    "movie_count": 8
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.7,
    "movie_rate_total": 141,
    "movie_count": 30
  },
  {
    "movie_id": 733,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 56,
    "movie_count": 12
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 70,
    "movie_count": 15
  },
  {
    "movie_id": 1028,
    "movie_rate_avg": 4.619047619047619,
    "movie_rate_total": 97,
    "movie_count": 21
  },
  {
    "movie_id": 3035,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 932,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 3548,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 32,
    "movie_count": 7
  },
  {
    "movie_id": 1035,
    "movie_rate_avg": 4.5625,
    "movie_rate_total": 73,
    "movie_count": 16
  },
  {
    "movie_id": 62,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 41,
    "movie_count": 9
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.551724137931035,
    "movie_rate_total": 132,
    "movie_count": 29
  },
  {
    "movie_id": 2125,
    "movie_rate_avg": 4.545454545454546,
    "movie_rate_total": 50,
    "movie_count": 11
  },
  {
    "movie_id": 914,
    "movie_rate_avg": 4.529411764705882,
    "movie_rate_total": 77,
    "movie_count": 17
  },
  {
    "movie_id": 953,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 45,
    "movie_count": 10
  },
  {
    "movie_id": 1873,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 27,
    "movie_count": 6
  },
  {
    "movie_id": 3034,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 27,
    "movie_count": 6
  },
  {
    "movie_id": 3148,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 45,
    "movie_count": 10
  }
]

MOVIE_OCP_10 = [
  {
    "movie_id": 2019,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 45,
    "movie_count": 9
  },
  {
    "movie_id": 1208,
    "movie_rate_avg": 4.894736842105263,
    "movie_rate_total": 93,
    "movie_count": 19
  },
  {
    "movie_id": 1213,
    "movie_rate_avg": 4.818181818181818,
    "movie_rate_total": 106,
    "movie_count": 22
  },
  {
    "movie_id": 916,
    "movie_rate_avg": 4.818181818181818,
    "movie_rate_total": 53,
    "movie_count": 11
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.730769230769231,
    "movie_rate_total": 123,
    "movie_count": 26
  },
  {
    "movie_id": 1206,
    "movie_rate_avg": 4.642857142857143,
    "movie_rate_total": 65,
    "movie_count": 14
  },
  {
    "movie_id": 2125,
    "movie_rate_avg": 4.615384615384615,
    "movie_rate_total": 60,
    "movie_count": 13
  },
  {
    "movie_id": 246,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 46,
    "movie_count": 10
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.590909090909091,
    "movie_rate_total": 101,
    "movie_count": 22
  },
  {
    "movie_id": 903,
    "movie_rate_avg": 4.588235294117647,
    "movie_rate_total": 78,
    "movie_count": 17
  },
  {
    "movie_id": 3000,
    "movie_rate_avg": 4.588235294117647,
    "movie_rate_total": 78,
    "movie_count": 17
  },
  {
    "movie_id": 3949,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 55,
    "movie_count": 12
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.575,
    "movie_rate_total": 183,
    "movie_count": 40
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 160,
    "movie_count": 35
  },
  {
    "movie_id": 3448,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 64,
    "movie_count": 14
  },
  {
    "movie_id": 1274,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 41,
    "movie_count": 9
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.55,
    "movie_rate_total": 91,
    "movie_count": 20
  },
  {
    "movie_id": 899,
    "movie_rate_avg": 4.55,
    "movie_rate_total": 91,
    "movie_count": 20
  },
  {
    "movie_id": 1252,
    "movie_rate_avg": 4.545454545454546,
    "movie_rate_total": 50,
    "movie_count": 11
  },
  {
    "movie_id": 3504,
    "movie_rate_avg": 4.538461538461538,
    "movie_rate_total": 59,
    "movie_count": 13
  }
]

MOVIE_OCP_11 = [
  {
    "movie_id": 912,
    "movie_rate_avg": 4.866666666666666,
    "movie_rate_total": 219,
    "movie_count": 45
  },
  {
    "movie_id": 1131,
    "movie_rate_avg": 4.714285714285714,
    "movie_rate_total": 33,
    "movie_count": 7
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.67741935483871,
    "movie_rate_total": 145,
    "movie_count": 31
  },
  {
    "movie_id": 1178,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 42,
    "movie_count": 9
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 84,
    "movie_count": 18
  },
  {
    "movie_id": 1267,
    "movie_rate_avg": 4.653846153846154,
    "movie_rate_total": 121,
    "movie_count": 26
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.6461538461538465,
    "movie_rate_total": 302,
    "movie_count": 65
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.636363636363637,
    "movie_rate_total": 102,
    "movie_count": 22
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.636363636363637,
    "movie_rate_total": 153,
    "movie_count": 33
  },
  {
    "movie_id": 3307,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 37,
    "movie_count": 8
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.616666666666666,
    "movie_rate_total": 277,
    "movie_count": 60
  },
  {
    "movie_id": 1221,
    "movie_rate_avg": 4.611111111111111,
    "movie_rate_total": 249,
    "movie_count": 54
  },
  {
    "movie_id": 951,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 69,
    "movie_count": 15
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.592592592592593,
    "movie_rate_total": 124,
    "movie_count": 27
  },
  {
    "movie_id": 1193,
    "movie_rate_avg": 4.589743589743589,
    "movie_rate_total": 179,
    "movie_count": 39
  },
  {
    "movie_id": 1284,
    "movie_rate_avg": 4.588235294117647,
    "movie_rate_total": 78,
    "movie_count": 17
  },
  {
    "movie_id": 3360,
    "movie_rate_avg": 4.588235294117647,
    "movie_rate_total": 78,
    "movie_count": 17
  },
  {
    "movie_id": 1276,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 110,
    "movie_count": 24
  },
  {
    "movie_id": 955,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 55,
    "movie_count": 12
  },
  {
    "movie_id": 3196,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 55,
    "movie_count": 12
  }
]

MOVIE_OCP_12 = [
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.7631578947368425,
    "movie_rate_total": 181,
    "movie_count": 38
  },
  {
    "movie_id": 1224,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 98,
    "movie_count": 21
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.6192660550458715,
    "movie_rate_total": 1007,
    "movie_count": 218
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.607142857142857,
    "movie_rate_total": 129,
    "movie_count": 28
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.578125,
    "movie_rate_total": 293,
    "movie_count": 64
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.576923076923077,
    "movie_rate_total": 238,
    "movie_count": 52
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.55,
    "movie_rate_total": 819,
    "movie_count": 180
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.545454545454546,
    "movie_rate_total": 350,
    "movie_count": 77
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.532786885245901,
    "movie_rate_total": 553,
    "movie_count": 122
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.528985507246377,
    "movie_rate_total": 625,
    "movie_count": 138
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.524096385542169,
    "movie_rate_total": 751,
    "movie_count": 166
  },
  {
    "movie_id": 1196,
    "movie_rate_avg": 4.47136563876652,
    "movie_rate_total": 1015,
    "movie_count": 227
  },
  {
    "movie_id": 1217,
    "movie_rate_avg": 4.464285714285714,
    "movie_rate_total": 125,
    "movie_count": 28
  },
  {
    "movie_id": 3429,
    "movie_rate_avg": 4.444444444444445,
    "movie_rate_total": 120,
    "movie_count": 27
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.443478260869565,
    "movie_rate_total": 511,
    "movie_count": 115
  },
  {
    "movie_id": 296,
    "movie_rate_avg": 4.438356164383562,
    "movie_rate_total": 648,
    "movie_count": 146
  },
  {
    "movie_id": 1358,
    "movie_rate_avg": 4.433333333333334,
    "movie_rate_total": 266,
    "movie_count": 60
  },
  {
    "movie_id": 541,
    "movie_rate_avg": 4.431372549019608,
    "movie_rate_total": 678,
    "movie_count": 153
  },
  {
    "movie_id": 1299,
    "movie_rate_avg": 4.425531914893617,
    "movie_rate_total": 208,
    "movie_count": 47
  }
]

MOVIE_OCP_13 = [
  {
    "movie_id": 497,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 3952,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 3019,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.739130434782608,
    "movie_rate_total": 109,
    "movie_count": 23
  },
  {
    "movie_id": 1253,
    "movie_rate_avg": 4.7272727272727275,
    "movie_rate_total": 52,
    "movie_count": 11
  },
  {
    "movie_id": 3469,
    "movie_rate_avg": 4.714285714285714,
    "movie_rate_total": 33,
    "movie_count": 7
  },
  {
    "movie_id": 2731,
    "movie_rate_avg": 4.714285714285714,
    "movie_rate_total": 33,
    "movie_count": 7
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.7,
    "movie_rate_total": 94,
    "movie_count": 20
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.7,
    "movie_rate_total": 94,
    "movie_count": 20
  },
  {
    "movie_id": 3634,
    "movie_rate_avg": 4.7,
    "movie_rate_total": 47,
    "movie_count": 10
  },
  {
    "movie_id": 2132,
    "movie_rate_avg": 4.7,
    "movie_rate_total": 47,
    "movie_count": 10
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.686274509803922,
    "movie_rate_total": 239,
    "movie_count": 51
  },
  {
    "movie_id": 2203,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 42,
    "movie_count": 9
  },
  {
    "movie_id": 944,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 28,
    "movie_count": 6
  },
  {
    "movie_id": 2804,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 84,
    "movie_count": 18
  },
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 70,
    "movie_count": 15
  },
  {
    "movie_id": 1237,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 42,
    "movie_count": 9
  },
  {
    "movie_id": 898,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 70,
    "movie_count": 15
  },
  {
    "movie_id": 3134,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 28,
    "movie_count": 6
  }
]

MOVIE_OCP_14 = [
  {
    "movie_id": 745,
    "movie_rate_avg": 4.739130434782608,
    "movie_rate_total": 109,
    "movie_count": 23
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.696428571428571,
    "movie_rate_total": 526,
    "movie_count": 112
  },
  {
    "movie_id": 1248,
    "movie_rate_avg": 4.684210526315789,
    "movie_rate_total": 89,
    "movie_count": 19
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.650485436893204,
    "movie_rate_total": 479,
    "movie_count": 103
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.642857142857143,
    "movie_rate_total": 260,
    "movie_count": 56
  },
  {
    "movie_id": 898,
    "movie_rate_avg": 4.631578947368421,
    "movie_rate_total": 88,
    "movie_count": 19
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.626086956521739,
    "movie_rate_total": 532,
    "movie_count": 115
  },
  {
    "movie_id": 1223,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 74,
    "movie_count": 16
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.617647058823529,
    "movie_rate_total": 157,
    "movie_count": 34
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.617647058823529,
    "movie_rate_total": 157,
    "movie_count": 34
  },
  {
    "movie_id": 1272,
    "movie_rate_avg": 4.615384615384615,
    "movie_rate_total": 120,
    "movie_count": 26
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.581818181818182,
    "movie_rate_total": 504,
    "movie_count": 110
  },
  {
    "movie_id": 2324,
    "movie_rate_avg": 4.573770491803279,
    "movie_rate_total": 279,
    "movie_count": 61
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.566929133858268,
    "movie_rate_total": 580,
    "movie_count": 127
  },
  {
    "movie_id": 951,
    "movie_rate_avg": 4.5625,
    "movie_rate_total": 73,
    "movie_count": 16
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.5588235294117645,
    "movie_rate_total": 155,
    "movie_count": 34
  },
  {
    "movie_id": 1193,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 369,
    "movie_count": 81
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.551020408163265,
    "movie_rate_total": 223,
    "movie_count": 49
  },
  {
    "movie_id": 1267,
    "movie_rate_avg": 4.545454545454546,
    "movie_rate_total": 150,
    "movie_count": 33
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.545454545454546,
    "movie_rate_total": 150,
    "movie_count": 33
  }
]

MOVIE_OCP_15 = [
  {
    "movie_id": 1945,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 42,
    "movie_count": 9
  },
  {
    "movie_id": 2329,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 56,
    "movie_count": 12
  },
  {
    "movie_id": 1136,
    "movie_rate_avg": 4.653846153846154,
    "movie_rate_total": 242,
    "movie_count": 52
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.648148148148148,
    "movie_rate_total": 251,
    "movie_count": 54
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.645161290322581,
    "movie_rate_total": 144,
    "movie_count": 31
  },
  {
    "movie_id": 3429,
    "movie_rate_avg": 4.642857142857143,
    "movie_rate_total": 65,
    "movie_count": 14
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.615384615384615,
    "movie_rate_total": 120,
    "movie_count": 26
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.612244897959184,
    "movie_rate_total": 226,
    "movie_count": 49
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 391,
    "movie_count": 85
  },
  {
    "movie_id": 1283,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 46,
    "movie_count": 10
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.578947368421052,
    "movie_rate_total": 87,
    "movie_count": 19
  },
  {
    "movie_id": 1203,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 64,
    "movie_count": 14
  },
  {
    "movie_id": 541,
    "movie_rate_avg": 4.568965517241379,
    "movie_rate_total": 265,
    "movie_count": 58
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 164,
    "movie_count": 36
  },
  {
    "movie_id": 1303,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 41,
    "movie_count": 9
  },
  {
    "movie_id": 913,
    "movie_rate_avg": 4.551724137931035,
    "movie_rate_total": 132,
    "movie_count": 29
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.537037037037037,
    "movie_rate_total": 245,
    "movie_count": 54
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.533333333333333,
    "movie_rate_total": 340,
    "movie_count": 75
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.53030303030303,
    "movie_rate_total": 299,
    "movie_count": 66
  }
]

MOVIE_OCP_16 = [
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.8076923076923075,
    "movie_rate_total": 125,
    "movie_count": 26
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 140,
    "movie_count": 30
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.612244897959184,
    "movie_rate_total": 452,
    "movie_count": 98
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.593406593406593,
    "movie_rate_total": 418,
    "movie_count": 91
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.592233009708738,
    "movie_rate_total": 473,
    "movie_count": 103
  },
  {
    "movie_id": 930,
    "movie_rate_avg": 4.578947368421052,
    "movie_rate_total": 87,
    "movie_count": 19
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.5777777777777775,
    "movie_rate_total": 206,
    "movie_count": 45
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.5777777777777775,
    "movie_rate_total": 206,
    "movie_count": 45
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.573529411764706,
    "movie_rate_total": 311,
    "movie_count": 68
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 160,
    "movie_count": 35
  },
  {
    "movie_id": 922,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 96,
    "movie_count": 21
  },
  {
    "movie_id": 1223,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 96,
    "movie_count": 21
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.553191489361702,
    "movie_rate_total": 214,
    "movie_count": 47
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.541666666666667,
    "movie_rate_total": 218,
    "movie_count": 48
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.529411764705882,
    "movie_rate_total": 385,
    "movie_count": 85
  },
  {
    "movie_id": 1293,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 135,
    "movie_count": 30
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 216,
    "movie_count": 48
  },
  {
    "movie_id": 1178,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 63,
    "movie_count": 14
  },
  {
    "movie_id": 1233,
    "movie_rate_avg": 4.491803278688525,
    "movie_rate_total": 274,
    "movie_count": 61
  },
  {
    "movie_id": 3730,
    "movie_rate_avg": 4.478260869565218,
    "movie_rate_total": 103,
    "movie_count": 23
  }
]

MOVIE_OCP_17 = [
  {
    "movie_id": 1254,
    "movie_rate_avg": 4.64,
    "movie_rate_total": 116,
    "movie_count": 25
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.633802816901408,
    "movie_rate_total": 987,
    "movie_count": 213
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.620253164556962,
    "movie_rate_total": 730,
    "movie_count": 158
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 320,
    "movie_count": 70
  },
  {
    "movie_id": 1217,
    "movie_rate_avg": 4.565217391304348,
    "movie_rate_total": 105,
    "movie_count": 23
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.552631578947368,
    "movie_rate_total": 173,
    "movie_count": 38
  },
  {
    "movie_id": 916,
    "movie_rate_avg": 4.541666666666667,
    "movie_rate_total": 109,
    "movie_count": 24
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.538461538461538,
    "movie_rate_total": 354,
    "movie_count": 78
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.529411764705882,
    "movie_rate_total": 154,
    "movie_count": 34
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.525925925925926,
    "movie_rate_total": 1222,
    "movie_count": 270
  },
  {
    "movie_id": 2028,
    "movie_rate_avg": 4.524017467248909,
    "movie_rate_total": 1036,
    "movie_count": 229
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.508982035928144,
    "movie_rate_total": 753,
    "movie_count": 167
  },
  {
    "movie_id": 2571,
    "movie_rate_avg": 4.503875968992248,
    "movie_rate_total": 1162,
    "movie_count": 258
  },
  {
    "movie_id": 953,
    "movie_rate_avg": 4.476190476190476,
    "movie_rate_total": 188,
    "movie_count": 42
  },
  {
    "movie_id": 2804,
    "movie_rate_avg": 4.475247524752476,
    "movie_rate_total": 452,
    "movie_count": 101
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.472527472527473,
    "movie_rate_total": 407,
    "movie_count": 91
  },
  {
    "movie_id": 898,
    "movie_rate_avg": 4.470588235294118,
    "movie_rate_total": 152,
    "movie_count": 34
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.462809917355372,
    "movie_rate_total": 540,
    "movie_count": 121
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.462686567164179,
    "movie_rate_total": 299,
    "movie_count": 67
  }
]

MOVIE_OCP_18 = [
  {
    "movie_id": 3516,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 25,
    "movie_count": 5
  },
  {
    "movie_id": 1281,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 20,
    "movie_count": 4
  },
  {
    "movie_id": 2401,
    "movie_rate_avg": 4.833333333333333,
    "movie_rate_total": 29,
    "movie_count": 6
  },
  {
    "movie_id": 1340,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 2644,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 3629,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 3037,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 3200,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 2010,
    "movie_rate_avg": 4.75,
    "movie_rate_total": 19,
    "movie_count": 4
  },
  {
    "movie_id": 1254,
    "movie_rate_avg": 4.714285714285714,
    "movie_rate_total": 33,
    "movie_count": 7
  },
  {
    "movie_id": 1136,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 70,
    "movie_count": 15
  },
  {
    "movie_id": 678,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 28,
    "movie_count": 6
  },
  {
    "movie_id": 110,
    "movie_rate_avg": 4.645161290322581,
    "movie_rate_total": 144,
    "movie_count": 31
  },
  {
    "movie_id": 913,
    "movie_rate_avg": 4.636363636363637,
    "movie_rate_total": 51,
    "movie_count": 11
  },
  {
    "movie_id": 1203,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 37,
    "movie_count": 8
  },
  {
    "movie_id": 1221,
    "movie_rate_avg": 4.619047619047619,
    "movie_rate_total": 97,
    "movie_count": 21
  },
  {
    "movie_id": 1248,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 46,
    "movie_count": 10
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 115,
    "movie_count": 25
  }
]

MOVIE_OCP_19 = [
  {
    "movie_id": 1292,
    "movie_rate_avg": 5.0,
    "movie_rate_total": 35,
    "movie_count": 7
  },
  {
    "movie_id": 2951,
    "movie_rate_avg": 4.8,
    "movie_rate_total": 24,
    "movie_count": 5
  },
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.75,
    "movie_rate_total": 38,
    "movie_count": 8
  },
  {
    "movie_id": 3504,
    "movie_rate_avg": 4.75,
    "movie_rate_total": 38,
    "movie_count": 8
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.714285714285714,
    "movie_rate_total": 33,
    "movie_count": 7
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.681818181818182,
    "movie_rate_total": 103,
    "movie_count": 22
  },
  {
    "movie_id": 162,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 42,
    "movie_count": 9
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 56,
    "movie_count": 12
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 28,
    "movie_count": 6
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 37,
    "movie_count": 8
  },
  {
    "movie_id": 950,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 37,
    "movie_count": 8
  },
  {
    "movie_id": 58,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 942,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 3088,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 2859,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 3741,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 934,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 23,
    "movie_count": 5
  },
  {
    "movie_id": 348,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 32,
    "movie_count": 7
  },
  {
    "movie_id": 2318,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 32,
    "movie_count": 7
  }
]

MOVIE_OCP_20 = [
  {
    "movie_id": 1178,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 84,
    "movie_count": 18
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.62962962962963,
    "movie_rate_total": 250,
    "movie_count": 54
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.629310344827586,
    "movie_rate_total": 537,
    "movie_count": 116
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.608695652173913,
    "movie_rate_total": 424,
    "movie_count": 92
  },
  {
    "movie_id": 922,
    "movie_rate_avg": 4.585365853658536,
    "movie_rate_total": 188,
    "movie_count": 41
  },
  {
    "movie_id": 899,
    "movie_rate_avg": 4.58,
    "movie_rate_total": 229,
    "movie_count": 50
  },
  {
    "movie_id": 3307,
    "movie_rate_avg": 4.56,
    "movie_rate_total": 114,
    "movie_count": 25
  },
  {
    "movie_id": 3095,
    "movie_rate_avg": 4.551724137931035,
    "movie_rate_total": 132,
    "movie_count": 29
  },
  {
    "movie_id": 3134,
    "movie_rate_avg": 4.526315789473684,
    "movie_rate_total": 86,
    "movie_count": 19
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.5227272727272725,
    "movie_rate_total": 199,
    "movie_count": 44
  },
  {
    "movie_id": 3022,
    "movie_rate_avg": 4.518518518518518,
    "movie_rate_total": 122,
    "movie_count": 27
  },
  {
    "movie_id": 2360,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 81,
    "movie_count": 18
  },
  {
    "movie_id": 2859,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 81,
    "movie_count": 18
  },
  {
    "movie_id": 1221,
    "movie_rate_avg": 4.494736842105263,
    "movie_rate_total": 427,
    "movie_count": 95
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.493333333333333,
    "movie_rate_total": 337,
    "movie_count": 75
  },
  {
    "movie_id": 1234,
    "movie_rate_avg": 4.492307692307692,
    "movie_rate_total": 292,
    "movie_count": 65
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.489583333333333,
    "movie_rate_total": 431,
    "movie_count": 96
  },
  {
    "movie_id": 1230,
    "movie_rate_avg": 4.483516483516484,
    "movie_rate_total": 408,
    "movie_count": 91
  },
  {
    "movie_id": 3629,
    "movie_rate_avg": 4.482758620689655,
    "movie_rate_total": 130,
    "movie_count": 29
  },
  {
    "movie_id": 1252,
    "movie_rate_avg": 4.481927710843373,
    "movie_rate_total": 372,
    "movie_count": 83
  }
]

MOVIE_AGE_1 = [
  {
    "movie_id": 1213,
    "movie_rate_avg": 4.84,
    "movie_rate_total": 121,
    "movie_count": 25
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.818181818181818,
    "movie_rate_total": 53,
    "movie_count": 11
  },
  {
    "movie_id": 1228,
    "movie_rate_avg": 4.714285714285714,
    "movie_rate_total": 66,
    "movie_count": 14
  },
  {
    "movie_id": 916,
    "movie_rate_avg": 4.6875,
    "movie_rate_total": 75,
    "movie_count": 16
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.68,
    "movie_rate_total": 117,
    "movie_count": 25
  },
  {
    "movie_id": 3000,
    "movie_rate_avg": 4.636363636363637,
    "movie_rate_total": 102,
    "movie_count": 22
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.636363636363637,
    "movie_rate_total": 51,
    "movie_count": 11
  },
  {
    "movie_id": 3949,
    "movie_rate_avg": 4.615384615384615,
    "movie_rate_total": 60,
    "movie_count": 13
  },
  {
    "movie_id": 903,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 115,
    "movie_count": 25
  },
  {
    "movie_id": 3462,
    "movie_rate_avg": 4.6,
    "movie_rate_total": 46,
    "movie_count": 10
  },
  {
    "movie_id": 1208,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 110,
    "movie_count": 24
  },
  {
    "movie_id": 3504,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 82,
    "movie_count": 18
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.543478260869565,
    "movie_rate_total": 209,
    "movie_count": 46
  },
  {
    "movie_id": 2125,
    "movie_rate_avg": 4.538461538461538,
    "movie_rate_total": 59,
    "movie_count": 13
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.526315789473684,
    "movie_rate_total": 86,
    "movie_count": 19
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.514285714285714,
    "movie_rate_total": 158,
    "movie_count": 35
  },
  {
    "movie_id": 2067,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 63,
    "movie_count": 14
  },
  {
    "movie_id": 1960,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 45,
    "movie_count": 10
  },
  {
    "movie_id": 1945,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 45,
    "movie_count": 10
  },
  {
    "movie_id": 1230,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 126,
    "movie_count": 28
  }
]

MOVIE_AGE_18 = [
  {
    "movie_id": 50,
    "movie_rate_avg": 4.6807980049875315,
    "movie_rate_total": 1877,
    "movie_count": 401
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.674568965517241,
    "movie_rate_total": 2169,
    "movie_count": 464
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.604938271604938,
    "movie_rate_total": 373,
    "movie_count": 81
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.568,
    "movie_rate_total": 571,
    "movie_count": 125
  },
  {
    "movie_id": 2324,
    "movie_rate_avg": 4.549180327868853,
    "movie_rate_total": 1110,
    "movie_count": 244
  },
  {
    "movie_id": 2858,
    "movie_rate_avg": 4.521678321678322,
    "movie_rate_total": 3233,
    "movie_count": 715
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.5195530726256985,
    "movie_rate_total": 809,
    "movie_count": 179
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.5054945054945055,
    "movie_rate_total": 1640,
    "movie_count": 364
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.472850678733032,
    "movie_rate_total": 1977,
    "movie_count": 442
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.471794871794872,
    "movie_rate_total": 872,
    "movie_count": 195
  },
  {
    "movie_id": 1213,
    "movie_rate_avg": 4.457912457912458,
    "movie_rate_total": 1324,
    "movie_count": 297
  },
  {
    "movie_id": 1193,
    "movie_rate_avg": 4.457831325301205,
    "movie_rate_total": 1110,
    "movie_count": 249
  },
  {
    "movie_id": 1252,
    "movie_rate_avg": 4.447368421052632,
    "movie_rate_total": 507,
    "movie_count": 114
  },
  {
    "movie_id": 2571,
    "movie_rate_avg": 4.446208112874779,
    "movie_rate_total": 2521,
    "movie_count": 567
  },
  {
    "movie_id": 1196,
    "movie_rate_avg": 4.442141623488774,
    "movie_rate_total": 2572,
    "movie_count": 579
  },
  {
    "movie_id": 1228,
    "movie_rate_avg": 4.43956043956044,
    "movie_rate_total": 404,
    "movie_count": 91
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.427046263345196,
    "movie_rate_total": 2488,
    "movie_count": 562
  },
  {
    "movie_id": 1218,
    "movie_rate_avg": 4.418181818181818,
    "movie_rate_total": 243,
    "movie_count": 55
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.415254237288136,
    "movie_rate_total": 521,
    "movie_count": 118
  }
]

MOVIE_AGE_25 = [
  {
    "movie_id": 318,
    "movie_rate_avg": 4.587699316628702,
    "movie_rate_total": 4028,
    "movie_count": 878
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.578520770010131,
    "movie_rate_total": 4519,
    "movie_count": 987
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.5740514075887395,
    "movie_rate_total": 3737,
    "movie_count": 817
  },
  {
    "movie_id": 260,
    "movie_rate_avg": 4.572695035460993,
    "movie_rate_total": 5158,
    "movie_count": 1128
  },
  {
    "movie_id": 50,
    "movie_rate_avg": 4.552429667519181,
    "movie_rate_total": 3560,
    "movie_count": 782
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.5495049504950495,
    "movie_rate_total": 919,
    "movie_count": 202
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.543859649122807,
    "movie_rate_total": 1295,
    "movie_count": 285
  },
  {
    "movie_id": 922,
    "movie_rate_avg": 4.516556291390729,
    "movie_rate_total": 682,
    "movie_count": 151
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.5162162162162165,
    "movie_rate_total": 1671,
    "movie_count": 370
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.509859154929577,
    "movie_rate_total": 1601,
    "movie_count": 355
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.485345838218054,
    "movie_rate_total": 3826,
    "movie_count": 853
  },
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.471337579617835,
    "movie_rate_total": 702,
    "movie_count": 157
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.4355509355509355,
    "movie_rate_total": 4267,
    "movie_count": 962
  },
  {
    "movie_id": 1221,
    "movie_rate_avg": 4.428134556574924,
    "movie_rate_total": 2896,
    "movie_count": 654
  },
  {
    "movie_id": 1262,
    "movie_rate_avg": 4.419689119170984,
    "movie_rate_total": 853,
    "movie_count": 193
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.419014084507042,
    "movie_rate_total": 1255,
    "movie_count": 284
  },
  {
    "movie_id": 1267,
    "movie_rate_avg": 4.418326693227091,
    "movie_rate_total": 1109,
    "movie_count": 251
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.415254237288136,
    "movie_rate_total": 1042,
    "movie_count": 236
  },
  {
    "movie_id": 1193,
    "movie_rate_avg": 4.412371134020619,
    "movie_rate_total": 2568,
    "movie_count": 582
  }
]

MOVIE_AGE_35 = [
  {
    "movie_id": 922,
    "movie_rate_avg": 4.6115702479338845,
    "movie_rate_total": 558,
    "movie_count": 121
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.585858585858586,
    "movie_rate_total": 908,
    "movie_count": 198
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.541935483870968,
    "movie_rate_total": 2112,
    "movie_count": 465
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.532894736842105,
    "movie_rate_total": 689,
    "movie_count": 152
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.510344827586207,
    "movie_rate_total": 1962,
    "movie_count": 435
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.4875,
    "movie_rate_total": 1795,
    "movie_count": 400
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.479245283018868,
    "movie_rate_total": 1187,
    "movie_count": 265
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.475538160469667,
    "movie_rate_total": 2287,
    "movie_count": 511
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.475247524752476,
    "movie_rate_total": 452,
    "movie_count": 101
  },
  {
    "movie_id": 1132,
    "movie_rate_avg": 4.47457627118644,
    "movie_rate_total": 264,
    "movie_count": 59
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.474226804123711,
    "movie_rate_total": 1302,
    "movie_count": 291
  },
  {
    "movie_id": 1131,
    "movie_rate_avg": 4.467741935483871,
    "movie_rate_total": 277,
    "movie_count": 62
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.457081545064377,
    "movie_rate_total": 2077,
    "movie_count": 466
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.450704225352113,
    "movie_rate_total": 632,
    "movie_count": 142
  },
  {
    "movie_id": 919,
    "movie_rate_avg": 4.446384039900249,
    "movie_rate_total": 1783,
    "movie_count": 401
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.44385026737968,
    "movie_rate_total": 831,
    "movie_count": 187
  },
  {
    "movie_id": 953,
    "movie_rate_avg": 4.440993788819876,
    "movie_rate_total": 715,
    "movie_count": 161
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.438287153652393,
    "movie_rate_total": 1762,
    "movie_count": 397
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.404040404040404,
    "movie_rate_total": 872,
    "movie_count": 198
  },
  {
    "movie_id": 923,
    "movie_rate_avg": 4.4,
    "movie_rate_total": 1122,
    "movie_count": 255
  }
]

MOVIE_AGE_45 = [
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.647058823529412,
    "movie_rate_total": 237,
    "movie_count": 51
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.607142857142857,
    "movie_rate_total": 129,
    "movie_count": 28
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.591549295774648,
    "movie_rate_total": 978,
    "movie_count": 213
  },
  {
    "movie_id": 1178,
    "movie_rate_avg": 4.56,
    "movie_rate_total": 114,
    "movie_count": 25
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.541666666666667,
    "movie_rate_total": 327,
    "movie_count": 72
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.50761421319797,
    "movie_rate_total": 888,
    "movie_count": 197
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.494949494949495,
    "movie_rate_total": 445,
    "movie_count": 99
  },
  {
    "movie_id": 904,
    "movie_rate_avg": 4.481481481481482,
    "movie_rate_total": 484,
    "movie_count": 108
  },
  {
    "movie_id": 318,
    "movie_rate_avg": 4.481283422459893,
    "movie_rate_total": 838,
    "movie_count": 187
  },
  {
    "movie_id": 2762,
    "movie_rate_avg": 4.4655172413793105,
    "movie_rate_total": 777,
    "movie_count": 174
  },
  {
    "movie_id": 1223,
    "movie_rate_avg": 4.461538461538462,
    "movie_rate_total": 116,
    "movie_count": 26
  },
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.4603174603174605,
    "movie_rate_total": 281,
    "movie_count": 63
  },
  {
    "movie_id": 1198,
    "movie_rate_avg": 4.443349753694581,
    "movie_rate_total": 902,
    "movie_count": 203
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.443298969072165,
    "movie_rate_total": 431,
    "movie_count": 97
  },
  {
    "movie_id": 3022,
    "movie_rate_avg": 4.4375,
    "movie_rate_total": 142,
    "movie_count": 32
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.436241610738255,
    "movie_rate_total": 661,
    "movie_count": 149
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.431818181818182,
    "movie_rate_total": 195,
    "movie_count": 44
  },
  {
    "movie_id": 919,
    "movie_rate_avg": 4.42948717948718,
    "movie_rate_total": 691,
    "movie_count": 156
  },
  {
    "movie_id": 969,
    "movie_rate_avg": 4.42948717948718,
    "movie_rate_total": 691,
    "movie_count": 156
  }
]

MOVIE_AGE_50 = [
  {
    "movie_id": 3030,
    "movie_rate_avg": 4.733333333333333,
    "movie_rate_total": 142,
    "movie_count": 30
  },
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.66,
    "movie_rate_total": 233,
    "movie_count": 50
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.6571428571428575,
    "movie_rate_total": 326,
    "movie_count": 70
  },
  {
    "movie_id": 913,
    "movie_rate_avg": 4.594594594594595,
    "movie_rate_total": 510,
    "movie_count": 111
  },
  {
    "movie_id": 745,
    "movie_rate_avg": 4.59375,
    "movie_rate_total": 147,
    "movie_count": 32
  },
  {
    "movie_id": 2203,
    "movie_rate_avg": 4.583333333333333,
    "movie_rate_total": 110,
    "movie_count": 24
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.567901234567901,
    "movie_rate_total": 740,
    "movie_count": 162
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.565476190476191,
    "movie_rate_total": 767,
    "movie_count": 168
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.551020408163265,
    "movie_rate_total": 446,
    "movie_count": 98
  },
  {
    "movie_id": 3134,
    "movie_rate_avg": 4.541666666666667,
    "movie_rate_total": 109,
    "movie_count": 24
  },
  {
    "movie_id": 3089,
    "movie_rate_avg": 4.541666666666667,
    "movie_rate_total": 109,
    "movie_count": 24
  },
  {
    "movie_id": 858,
    "movie_rate_avg": 4.540404040404041,
    "movie_rate_total": 899,
    "movie_count": 198
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.53125,
    "movie_rate_total": 290,
    "movie_count": 64
  },
  {
    "movie_id": 750,
    "movie_rate_avg": 4.53030303030303,
    "movie_rate_total": 598,
    "movie_count": 132
  },
  {
    "movie_id": 2732,
    "movie_rate_avg": 4.521739130434782,
    "movie_rate_total": 104,
    "movie_count": 23
  },
  {
    "movie_id": 3022,
    "movie_rate_avg": 4.518518518518518,
    "movie_rate_total": 122,
    "movie_count": 27
  },
  {
    "movie_id": 922,
    "movie_rate_avg": 4.510204081632653,
    "movie_rate_total": 221,
    "movie_count": 49
  },
  {
    "movie_id": 3435,
    "movie_rate_avg": 4.507936507936508,
    "movie_rate_total": 284,
    "movie_count": 63
  },
  {
    "movie_id": 969,
    "movie_rate_avg": 4.50354609929078,
    "movie_rate_total": 635,
    "movie_count": 141
  },
  {
    "movie_id": 1178,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 144,
    "movie_count": 32
  }
]

MOVIE_AGE_56 = [
  {
    "movie_id": 1148,
    "movie_rate_avg": 4.722222222222222,
    "movie_rate_total": 85,
    "movie_count": 18
  },
  {
    "movie_id": 1237,
    "movie_rate_avg": 4.666666666666667,
    "movie_rate_total": 98,
    "movie_count": 21
  },
  {
    "movie_id": 3469,
    "movie_rate_avg": 4.625,
    "movie_rate_total": 111,
    "movie_count": 24
  },
  {
    "movie_id": 1207,
    "movie_rate_avg": 4.6231884057971016,
    "movie_rate_total": 319,
    "movie_count": 69
  },
  {
    "movie_id": 527,
    "movie_rate_avg": 4.62043795620438,
    "movie_rate_total": 633,
    "movie_count": 137
  },
  {
    "movie_id": 912,
    "movie_rate_avg": 4.598039215686274,
    "movie_rate_total": 469,
    "movie_count": 102
  },
  {
    "movie_id": 919,
    "movie_rate_avg": 4.573170731707317,
    "movie_rate_total": 375,
    "movie_count": 82
  },
  {
    "movie_id": 969,
    "movie_rate_avg": 4.572916666666667,
    "movie_rate_total": 439,
    "movie_count": 96
  },
  {
    "movie_id": 1066,
    "movie_rate_avg": 4.571428571428571,
    "movie_rate_total": 64,
    "movie_count": 14
  },
  {
    "movie_id": 3089,
    "movie_rate_avg": 4.555555555555555,
    "movie_rate_total": 82,
    "movie_count": 18
  },
  {
    "movie_id": 899,
    "movie_rate_avg": 4.551724137931035,
    "movie_rate_total": 264,
    "movie_count": 58
  },
  {
    "movie_id": 3095,
    "movie_rate_avg": 4.547169811320755,
    "movie_rate_total": 241,
    "movie_count": 53
  },
  {
    "movie_id": 913,
    "movie_rate_avg": 4.53921568627451,
    "movie_rate_total": 463,
    "movie_count": 102
  },
  {
    "movie_id": 1293,
    "movie_rate_avg": 4.531914893617022,
    "movie_rate_total": 213,
    "movie_count": 47
  },
  {
    "movie_id": 1250,
    "movie_rate_avg": 4.517647058823529,
    "movie_rate_total": 384,
    "movie_count": 85
  },
  {
    "movie_id": 2019,
    "movie_rate_avg": 4.513513513513513,
    "movie_rate_total": 167,
    "movie_count": 37
  },
  {
    "movie_id": 1254,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 207,
    "movie_count": 46
  },
  {
    "movie_id": 1212,
    "movie_rate_avg": 4.5,
    "movie_rate_total": 234,
    "movie_count": 52
  },
  {
    "movie_id": 1945,
    "movie_rate_avg": 4.490909090909091,
    "movie_rate_total": 247,
    "movie_count": 55
  },
  {
    "movie_id": 1204,
    "movie_rate_avg": 4.4875,
    "movie_rate_total": 359,
    "movie_count": 80
  }
]


# def TMDBMOVIEDATA(request):
#   count1 = 0
#   count2 = 0 
#   count3 = 417
#   for movie in MOVIE_LIST:
#     count3 += 1 
#     print(movie["movie_id"])
#     find_movie = Moviedata.objects.get(movieId = movie["movie_id"])
#     find_movie = find_movie.tmdbId
#     URL = f'https://api.themoviedb.org/3/movie/{find_movie}/recommendations'

#     params = {
#         'api_key' : 'bd3e649e69462e2b66f7c2580fdd5a83',
#         'language' : 'ko-kr'
#     }
#     recommendmovies = requests.get(URL, params=params)
#     recommendmoviesjson = recommendmovies.json()
#     recommendations = []
#     for i in range(len(recommendmoviesjson.get('results'))):
#         recommendations.append(str(recommendmoviesjson.get('results')[i].get('id')))
#     for movie_id in recommendations:
#       URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}'
#       params = {
#           'api_key' : 'bd3e649e69462e2b66f7c2580fdd5a83',
#           'language' : 'ko-kr'
#       }
#       #https://image.tmdb.org/t/p/original/{poster_path}.jpg
#       movie = requests.get(URL2, params=params)
#       moviejson = movie.json()
#       title = moviejson['title']
#       if Movie.objects.filter(title=title).exists():
#         pass
#       else:
#         id = moviejson['id']
#         overview = moviejson['overview']
#         release_date = moviejson['release_date']
#         vote_average = moviejson['vote_average']
#         if moviejson['poster_path'] :
#           poster_path = 'https://image.tmdb.org/t/p/original'+ moviejson['poster_path']
#         else :
#           poster_path = ''
#         budget = moviejson['budget']
#         revenue = moviejson['revenue']
#         movie = Movie(
#           id = id,
#           title = title, 
#           overview = overview,
#           release_date = release_date, 
#           vote_average = vote_average,
#           poster_path = poster_path,
#           budget = budget,
#           revenue = revenue 
#           )
#         movie.save()
#     print(f'{count3}/600 완료')
#   return HttpResponse('Success convert json to database')


# def get_movie_data(request):
#     # json 파일 불러옴
#     with open('movies/movieiddata.json') as f:

#         data = json.loads(f.read())

#     # dataFrame 변환
#     df = pd.json_normalize(data)

#     for idx, row in df.iterrows():
#         # Movie table에 저장
#         Moviedata.objects.create(movieId=row['movieId'], tmdbId=row['tmdbId'])

#     return HttpResponse('Success convert json to database')

# def get_user_data(request):
#     # json 파일 불러옴
#     with open('movies/users.json') as f:

#         data = json.loads(f.read())

#     # dataFrame 변환
#     df = pd.json_normalize(data)

#     for idx, row in df.iterrows():
#         # Movie table에 저장
#         Userdata.objects.create(id=row['id'], gender=row['gender'],
#                              age=row['age'], occupation = row['occupation'])

#     return HttpResponse('Success convert json to database')


# def get_rate_data(request):
#     # json 파일 불러옴
#     with open('movies/rate.json') as f:

#         data = json.loads(f.read())

#     # dataFrame 변환
#     df = pd.json_normalize(data)

#     for idx, row in df.iterrows():
#         # Movie table에 저장
#         userdata = Userdata.objects.get(pk=row['user_id'])
#         moviedata = Moviedata.objects.get(pk=row['movie_id'])
#         Rate.objects.create(user_id=userdata, movie_id=moviedata,
#                              rate=row['rate'])

#     return HttpResponse('Success convert json to database')


# 성별 영화 추천
# def movies_cost_effective(request, gender):
#     users = get_list_or_404(Userdata, gender=gender)
#     # 각 아이디들 영화 조회 및 점수 추가
#     rates = Rate.objects.all()
#     movies = [{
#         'movie_id': 0,
#         'movie_rate': 0,
#         'movie_total': 0,
#         'movie_count': 0,
#         }]
#     for user in users:
#         for rate in rates:
#             if user.id == rate.user_id:
#                 # 영화가 이전에 들어갔었다면
#                 for movie in movies:
#                     if rate.movie_id == movie['movie_id']:
#                         movie['movie_total'] += rate.rate
#                         movie['movie_count'] += 1
#                         movie['movie_rate'] = movie['movie_total'] / movie['movie_count']
                        
#                     else:
#                         movies += [{
#                             'movie_id': rate.movie_id,
#                             'movie_rate': rate.rate,
#                             'movie_total': rate.rate,
#                             'movie_count': 1,
#                             }]
#     movies = sorted(movies, key=lambda k: -k['movie_rate'])[:20]
#     print(movies)

@require_http_methods(['GET'])
def gender_list(request, username):
  user = User.objects.get(username=username)
  if user.gender == 'F':
    movies = MOVIE_FEMALE
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  else:
    movies = MOVIE_MALE
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  
  find_movie = Moviedata.objects.get(movieId = movie_id)
  movie_id = find_movie.tmdbId

  URL = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'

  params = {
        'api_key' : 'bd3e649e69462e2b66f7c2580fdd5a83',
        'language' : 'ko-kr'
    }

  recommendmovies = requests.get(URL, params=params)
  recommendmovies = recommendmovies.json()

   # print(recommendmovies['results'])
  movies_again = recommendmovies['results']
  movie_id_again = random.choice(movies_again)['id']
  
  URL = f'https://api.themoviedb.org/3/movie/{movie_id_again}/similar'

  recommendmovies = requests.get(URL, params=params)
  recommendmovies = recommendmovies.json()
  return JsonResponse(recommendmovies, json_dumps_params={'ensure_ascii': False})


# @login_required
@require_http_methods(['GET'])
def occupation_list(request, username):
  user = User.objects.get(username=username)
  if user.occupation == '0':
    movies = MOVIE_OCP_00
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '1':
    movies = MOVIE_OCP_01
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '2':
    movies = MOVIE_OCP_02
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '3':
    movies = MOVIE_OCP_03
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '4':
    movies = MOVIE_OCP_04
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '5':
    movies = MOVIE_OCP_05
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '6':
    movies = MOVIE_OCP_06
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '7':
    movies = MOVIE_OCP_07
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '8':
    movies = MOVIE_OCP_08
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '9':
    movies = MOVIE_OCP_09
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '10':
    movies = MOVIE_OCP_10
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '11':
    movies = MOVIE_OCP_11
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '12':
    movies = MOVIE_OCP_12
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '13':
    movies = MOVIE_OCP_13
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '14':
    movies = MOVIE_OCP_14
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '15':
    movies = MOVIE_OCP_15
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '16':
    movies = MOVIE_OCP_16
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '17':
    movies = MOVIE_OCP_17
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '18':
    movies = MOVIE_OCP_18
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '19':
    movies = MOVIE_OCP_19
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif user.occupation == '20':
    movies = MOVIE_OCP_20
    movie = random.choice(movies)
    movie_id = movie['movie_id']

  find_movie = Moviedata.objects.get(movieId = movie_id)
  movie_id = find_movie.tmdbId
  
  URL = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'

  params = {
        'api_key' : 'bd3e649e69462e2b66f7c2580fdd5a83',
        'language' : 'ko-kr'
    }

  recommendmovies = requests.get(URL, params=params)
  recommendmovies = recommendmovies.json()

  # print(recommendmovies['results'])
  movies_again = recommendmovies['results']
  movie_id_again = random.choice(movies_again)['id']

  URL = f'https://api.themoviedb.org/3/movie/{movie_id_again}/similar'

  recommendmovies = requests.get(URL, params=params)
  recommendmovies = recommendmovies.json()

  return JsonResponse(recommendmovies, json_dumps_params={'ensure_ascii': False})




def age_list(request, username):
  
  user = User.objects.get(username=username)
  if user.age < 18:
    movies = MOVIE_AGE_1
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif 18 <= user.age < 25:
    movies = MOVIE_AGE_18
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif 25 <= user.age < 34:
    movies = MOVIE_AGE_25
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif 34 <= user.age < 45:
    movies = MOVIE_AGE_35
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif 45 <= user.age < 49:
    movies = MOVIE_AGE_45
    movie = random.choice(movies)
    movie_id = movie['movie_id']
  elif 50 <= user.age < 56:
    movies = MOVIE_AGE_50
    movie = random.choice(movies)
    movie_id = movie['movie_id']  
  elif 56 <= user.age:
    movies = MOVIE_AGE_56
    movie = random.choice(movies)
    movie_id = movie['movie_id'] 
  
  find_movie = Moviedata.objects.get(movieId = movie_id)
  movie_id = find_movie.tmdbId

  URL = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'

  params = {
        'api_key' : 'bd3e649e69462e2b66f7c2580fdd5a83',
        'language' : 'ko-kr'
    }

  recommendmovies = requests.get(URL, params=params)
  recommendmovies = recommendmovies.json()

   # print(recommendmovies['results'])
  movies_again = recommendmovies['results']
  movie_id_again = random.choice(movies_again)['id']
  
  URL = f'https://api.themoviedb.org/3/movie/{movie_id_again}/similar'

  recommendmovies = requests.get(URL, params=params)
  recommendmovies = recommendmovies.json()

  return JsonResponse(recommendmovies, json_dumps_params={'ensure_ascii': False})


# @login_required
@require_http_methods(['GET'])
def search(request, movie_title):
    # 이미 영화가 있다면, 조회 및 내보내기
  URL = f'https://api.themoviedb.org/3/search/movie'
  params = {
      'api_key' : 'bd3e649e69462e2b66f7c2580fdd5a83',
      'language' : 'ko-kr',
      'query': f'{movie_title}'
  }
  data_json = requests.get(URL, params=params)
  data_json = data_json.json()
  # 받아온 데이터들 보여주기전에 데이터 베이스에 저장
  # 형태
  # {
  #     'page': 1
  #     'results':[
  #         {
  #             영화
  #         },
  #         {
  #             영화
  #         }
  #     ]
  # }
  # for movie in data_json['results']:
  #     # 받아온 데이터 중에 영화가 데이터베이스에 존재한다면 패스
  #     if Movie.objects.filter(id=movie['id']).exists():
  #         pass
  #     else:
  #         id = movie['id']
  #         title = movie['title']
  #         overview = movie['overview']
  #         release_date = movie['release_date']
  #         vote_average = movie['vote_average']
  #         if movie['poster_path'] :
  #             poster_path = 'https://image.tmdb.org/t/p/original'+ movie['poster_path']
  #         else :
  #             poster_path = ''
  #         budget = movie['budget']
  #         revenue = movie['revenue']
  #         data = Movie(
  #             id = id,
  #             title = title, 
  #             overview = overview,
  #             release_date = release_date, 
  #             vote_average = vote_average,
  #             poster_path = poster_path,
  #             budget = budget,
  #             revenue = revenue 
  #             )
  #         data.save()
  # data_json = data_json.json()
  return JsonResponse(data_json, json_dumps_params={'ensure_ascii': False})

# @login_required
@require_http_methods(['GET'])
def detail(request, movie_id):
  if Movie.objects.filter(id=movie_id).exists():
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data)
    # 시리얼라이저에 Youtube API 데이터 추가 필요 (스포 포함/ 미포함)
  else : 
    URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {
        'api_key' : 'bd3e649e69462e2b66f7c2580fdd5a83',
        'language' : 'ko-kr'
    }
    movie = requests.get(URL2, params=params)
    moviejson = movie.json()
    id = moviejson['id']
    title = moviejson['title']
    adult = moviejson['adult']
    budget = moviejson['budget']
    if moviejson['backdrop_path'] :
      backdrop_path = 'https://image.tmdb.org/t/p/original'+ moviejson['backdrop_path']
    else :
      backdrop_path = ''
    genres = moviejson['genres']
    runtime = moviejson['runtime']
    tagline = moviejson['tagline']
    overview = moviejson['overview']
    release_date = moviejson['release_date']
    vote_average = moviejson['vote_average']
    if moviejson['poster_path'] :
      poster_path = 'https://image.tmdb.org/t/p/original'+ moviejson['poster_path']
    else :
      poster_path = ''
    revenue = moviejson['revenue']
    movie = Movie(
      id = id,
      title = title, 
      adult = adult,
      budget = budget,
      backdrop_path = backdrop_path,
      genres = genres,
      runtime = runtime,
      tagline = tagline,
      overview = overview,
      release_date = release_date, 
      vote_average = vote_average,
      poster_path = poster_path,
      revenue = revenue 
      )
    movie.save()
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data)


@api_view(['POST'])
def review_create(request, movie_id):
  user = request.user
  movie = Movie.objects.get(id=movie_id)
  print(movie)
  # movie_id, user_id, rate, content
  serializer = ReviewSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
      serializer.save(movie=movie, user=user)
      reviews = movie.review_set.all()
      # movie_after = Movie.objects.get(id=movie_id)
      serializer = ReviewSerializer(reviews, many=True)
      print(serializer.data)
      return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)



@api_view(['DELETE'])
def review_delete(request, review_id):
    review = Review.objects.get(id=review_id)
    movie_id = review.movie_id
    print(movie_id)
    review.delete()
    movie = Movie.objects.get(id=movie_id)
    review = movie.review_set.all()
    serializer = ReviewSerializer(review, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['PUT'])
def review_update(request, review_id):
    review = Review.objects.get(id=review_id)
    movie_id = review.movie_id
    if request.user == review.user:
      serializer = ReviewSerializer(instance=review, data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        movie = Movie.objects.get(id=movie_id)
        review = movie.review_set.all()
        serializer = ReviewSerializer(review, many=True)
        return JsonResponse(serializer.data, safe=False)






# 뷰 -> 로그인아이디 조회가능
# Json변환
# Django록 보내준다는게 나이 별 영화 조회request.user 
# 영화조회
# 아이디 -> 장고내에서 accounts접근
# age, 영화 추천


final_lst = []
@require_http_methods(['GET'])
def costeffective_list(request):
  global final_lst

  movies = Movie.objects.all()
  movies_lst = []

  if len(final_lst) == 0:
    for movie in movies:
      # print(movie)
      if movie.budget == 0 or movie.revenue == 0 or movie.poster_path == False:
        pass
      else:
        movie_costeffective = (movie.revenue - movie.budget) + (movie.revenue // movie.budget)
        # print(movie.title, movie_costeffective)
        movies_lst += [(movie_costeffective, movie.id, movie.poster_path)]
    final_lst = sorted(movies_lst, key=lambda student: student[0], reverse=True)[:40]
  picked_lst = random.sample(final_lst, 20)
   
  

  return JsonResponse(picked_lst, safe=False, json_dumps_params={'ensure_ascii': False})