"""
Supplies the get_x_y function for task 1.2.3

Adapted from: http://www.wolframalpha.com/input/?i=pikachu-like+curve
"""
import numpy as np


def _UnitStep(x):
    return np.heaviside(x.real, 1)

def _x(t):
    return (((-1/4 * np.sin(10/7 - 23 * t) -
     3/10 * np.sin(4/3 - 22 * t) -
     2/5 * np.sin(7/5 - 19 * t) -
     1/5 * np.sin(7/5 - 16 * t) -
     3/7 * np.sin(10/7 - 15 * t) -
     3/8 * np.sin(13/9 - 9 * t) -
     19/13 * np.sin(11/7 - 3 * t) +
     222/5 * np.sin(t + 11/7) +
     41/2 * np.sin(2 * t + 11/7) +
     34/9 * np.sin(4 * t + 11/7) +
     1/3 * np.sin(5 * t + 8/5) +
     3/8 * np.sin(6 * t + 8/5) +
     12/7 * np.sin(7 * t + 13/8) +
     11/7 * np.sin(8 * t + 13/8) +
     1/4 * np.sin(10 * t + 20/13) +
     2/9 * np.sin(11 * t + 16/9) +
     3/8 * np.sin(12 * t + 8/5) +
     1/3 * np.sin(13 * t + 7/4) +
     1/2 * np.sin(14 * t + 17/10) +
     5/7 * np.sin(17 * t + 17/10) +
     1/28 * np.sin(18 * t + 9/2) +
     1/2 * np.sin(20 * t + 12/7) +
     3/7 * np.sin(21 * t + 16/9) +
     6/11 * np.sin(24 * t + 7/4) -
     979/9) * _UnitStep(51 * np.pi - t) * _UnitStep(t - 47 * np.pi) +
     (-6/5 * np.sin(14/9 - 22 * t) -
     1/9 * np.sin(7/5 - 19 * t) -
     9/8 * np.sin(14/9 - 18 * t) -
     1/14 * np.sin(15/11 - 15 * t) -
     6/5 * np.sin(11/7 - 12 * t) -
     7/6 * np.sin(11/7 - 8 * t) -
     29/10 * np.sin(11/7 - 6 * t) -
     104/3 * np.sin(11/7 - 2 * t) +
     415/18 * np.sin(t + 11/7) +
     71/18 * np.sin(3 * t + 11/7) +
     19/8 * np.sin(4 * t + 33/7) +
     22/21 * np.sin(5 * t + 8/5) +
     3/8 * np.sin(7 * t + 61/13) +
     5/9 * np.sin(9 * t + 11/7) +
     1/8 * np.sin(10 * t + 14/3) +
     4/7 * np.sin(11 * t + 11/7) +
     4/11 * np.sin(13 * t + 14/3) +
     1/7 * np.sin(14 * t + 14/3) +
     2/7 * np.sin(16 * t + 5/3) +
     1/6 * np.sin(17 * t + 5/3) +
     6/7 * np.sin(20 * t + 8/5) +
     1/7 * np.sin(21 * t + 5/3) +
     1/6 * np.sin(23 * t + 8/5) -
     2765/8) * _UnitStep(47 * np.pi - t) * _UnitStep(t - 43 * np.pi) +
     (1189/22 * np.sin(t + 11/7) +
     3/4 * np.sin(2 * t + 13/8) +
     11/2 * np.sin(3 * t + 8/5) +
     2/7 * np.sin(4 * t + 17/7) +
     22/9 * np.sin(5 * t + 18/11) +
     1/4 * np.sin(6 * t + 17/7) +
     16/17 * np.sin(7 * t + 20/11) +
     1/5 * np.sin(8 * t + 29/9) -
     1627/7) * _UnitStep(43 * np.pi - t) * _UnitStep(t - 39 * np.pi) +
     (-3/7 * np.sin(1/18 - 5 * t) -
     3/4 * np.sin(1/2 - 3 * t) +
     109/9 * np.sin(t + 13/10) +
     5/8 * np.sin(2 * t + 11/3) +
     5/9 * np.sin(4 * t + 10/3) +
     3/10 * np.sin(6 * t + 21/8) +
     2/9 * np.sin(7 * t + 2/3) +
     1/4 * np.sin(8 * t + 23/8) -
     1190/9) * _UnitStep(39 * np.pi - t) * _UnitStep(t - 35 * np.pi) +
     (188/21 * np.sin(t + 27/28) +
     2/5 * np.sin(2 * t + 17/6) +
     2/3 * np.sin(3 * t + 91/23) +
     3/8 * np.sin(4 * t + 53/18) +
     2/11 * np.sin(5 * t + 1/7) -
     369) * _UnitStep(35 * np.pi - t) * _UnitStep(t - 31 * np.pi) +
     (-8/9 * np.sin(1/10 - 12 * t) -
     34/9 * np.sin(10/9 - 6 * t) -
     137/10 * np.sin(5/7 - 2 * t) +
     26/5 * np.sin(t + 13/4) +
     118/5 * np.sin(3 * t + 11/8) +
     43/8 * np.sin(4 * t + 13/7) +
     49/6 * np.sin(5 * t + 11/12) +
     22/5 * np.sin(7 * t + 13/4) +
     17/16 * np.sin(8 * t + 1/7) +
     5/4 * np.sin(9 * t + 1/4) +
     5/7 * np.sin(10 * t + 17/5) +
     29/15 * np.sin(11 * t + 5/6) -
     1915/8) * _UnitStep(31 * np.pi - t) * _UnitStep(t - 27 * np.pi) +
     (-2/7 * np.sin(10/7 - 7 * t) -
     np.sin(1/27 - 4 * t) +
     68/7 * np.sin(t + 44/15) +
     76/9 * np.sin(2 * t + 37/10) +
     30/7 * np.sin(3 * t + 1) +
     8/9 * np.sin(5 * t + 3/2) +
     4/5 * np.sin(6 * t + 31/8) +
     3/7 * np.sin(8 * t + 10/3) +
     6/13 * np.sin(9 * t + 8/7) +
     1/3 * np.sin(10 * t + 31/9) -
     2135/9) * _UnitStep(27 * np.pi - t) * _UnitStep(t - 23 * np.pi) +
     (-3/8 * np.sin(1/4 - 23 * t) -
     3/5 * np.sin(1/8 - 22 * t) -
     13/8 * np.sin(5/4 - 20 * t) -
     9/7 * np.sin(3/2 - 16 * t) -
     41/5 * np.sin(4/3 - 4 * t) +
     768/7 * np.sin(t + 11/5) +
     109/5 * np.sin(2 * t + 16/7) +
     150/13 * np.sin(3 * t + 11/6) +
     33/7 * np.sin(5 * t + 97/24) +
     23/4 * np.sin(6 * t + 5/7) +
     69/7 * np.sin(7 * t + 9/8) +
     32/5 * np.sin(8 * t + 21/5) +
     7/6 * np.sin(9 * t + 22/9) +
     28/5 * np.sin(10 * t + 5/6) +
     43/10 * np.sin(11 * t + 26/7) +
     14/9 * np.sin(12 * t + 5/11) +
     13/9 * np.sin(13 * t + 40/9) +
     11/6 * np.sin(14 * t + 2/5) +
     3/2 * np.sin(15 * t + 17/10) +
     7/11 * np.sin(17 * t + 4/3) +
     3/8 * np.sin(18 * t + 31/10) +
     4/7 * np.sin(19 * t + 14/9) +
     6/5 * np.sin(21 * t + 17/7) +
     4/7 * np.sin(24 * t + 27/8) +
     1006/11) * _UnitStep(23 * np.pi - t) * _UnitStep(t - 19 * np.pi) +
     (-63/8 * np.sin(2/7 - 8 * t) -
     38/13 * np.sin(11/9 - 6 * t) -
     14/5 * np.sin(1/17 - 4 * t) +
     77/9 * np.sin(t + 1/2) +
     52/7 * np.sin(2 * t + 10/3) +
     22/9 * np.sin(3 * t + 76/17) +
     21/8 * np.sin(5 * t + 26/7) +
     3 * np.sin(7 * t + 15/8) +
     64/7 * np.sin(9 * t + 57/14) +
     6 * np.sin(10 * t + 17/6) -
     544/7) * _UnitStep(19 * np.pi - t) * _UnitStep(t - 15 * np.pi) +
     (-37/10 * np.sin(4/7 - 5 * t) -
     3 * np.sin(3/7 - 3 * t) +
     24/7 * np.sin(t + 7/6) +
     9/7 * np.sin(2 * t + 2/5) +
     31/15 * np.sin(4 * t + 37/8) +
     9/5 * np.sin(6 * t + 12/5) +
     59/12 * np.sin(7 * t + 13/6) +
     15/7 * np.sin(8 * t + 25/8) +
     134/15 * np.sin(9 * t + 7/3) +
     73/8 * np.sin(10 * t + 1/5) -
     4406/11) * _UnitStep(15 * np.pi - t) * _UnitStep(t - 11 * np.pi) +
     (236/7 * np.sin(t + 6/5) +
     1/2 * np.sin(2 * t + 47/12) -
     627/5) * _UnitStep(11 * np.pi - t) * _UnitStep(t - 7 * np.pi) +
     (69/2 * np.sin(t + 5/6) -
     715/2) * _UnitStep(7 * np.pi - t) * _UnitStep(t - 3 * np.pi) +
     (-19/9 * np.sin(6/5 - 21 * t) -
     37/10 * np.sin(7/9 - 19 * t) -
     23/8 * np.sin(1 - 17 * t) -
     16/3 * np.sin(7/6 - 16 * t) -
     29/5 * np.sin(1/5 - 9 * t) -
     919/11 * np.sin(1/7 - 3 * t) +
     1573/6 * np.sin(t + 91/45) +
     214/5 * np.sin(2 * t + 33/8) +
     421/14 * np.sin(4 * t + 13/8) +
     61/6 * np.sin(5 * t + 19/5) +
     401/16 * np.sin(6 * t + 43/14) +
     511/51 * np.sin(7 * t + 35/8) +
     144/7 * np.sin(8 * t + 5/6) +
     137/10 * np.sin(10 * t + 25/13) +
     18/7 * np.sin(11 * t + 15/7) +
     17/9 * np.sin(12 * t + 41/9) +
     9/7 * np.sin(13 * t + 13/7) +
     29/10 * np.sin(14 * t + 22/7) +
     25/8 * np.sin(15 * t + 1/4) +
     12/5 * np.sin(18 * t + 11/8) +
     14/5 * np.sin(20 * t + 27/7) +
     13/8 * np.sin(22 * t + 12/7) +
     7/6 * np.sin(23 * t + 7/9) +
     26/11 * np.sin(24 * t + 23/7) -
     1891/8) * _UnitStep(3 * np.pi - t) * _UnitStep(t + np.pi)) * _UnitStep(np.sqrt(np.sign(np.sin(t/2))))).real

def _y(t):
    return (((-8/11 * np.sin(11/8 - 22 * t) -
     1/2 * np.sin(10/7 - 21 * t) +
     67/6 * np.sin(t + 33/7) +
     1478/29 * np.sin(2 * t + 11/7) +
     3/5 * np.sin(3 * t + 30/7) +
     26/3 * np.sin(4 * t + 11/7) +
     1/6 * np.sin(5 * t + 13/9) +
     30/29 * np.sin(6 * t + 8/5) +
     2/5 * np.sin(7 * t + 14/3) +
     88/29 * np.sin(8 * t + 8/5) +
     1/4 * np.sin(9 * t + 31/7) +
     11/8 * np.sin(10 * t + 8/5) +
     1/16 * np.sin(11 * t + 9/2) +
     1/12 * np.sin(12 * t + 5/4) +
     1/10 * np.sin(13 * t + 25/11) +
     11/8 * np.sin(14 * t + 18/11) +
     2/7 * np.sin(15 * t + 37/8) +
     1/6 * np.sin(16 * t + 11/8) +
     2/9 * np.sin(17 * t + 5/3) +
     1/5 * np.sin(18 * t + 17/10) +
     1/13 * np.sin(19 * t + 19/8) +
     23/24 * np.sin(20 * t + 12/7) +
     7/11 * np.sin(23 * t + 9/5) +
     9/7 * np.sin(24 * t + 7/4) -
     1538/7) * _UnitStep(51 * np.pi - t) * _UnitStep(t - 47 * np.pi) +
     (-2/7 * np.sin(20/13 - 23 * t) -
     1/6 * np.sin(3/2 - 20 * t) -
     5/7 * np.sin(20/13 - 17 * t) -
     1/9 * np.sin(20/13 - 11 * t) -
     1/6 * np.sin(13/9 - 9 * t) -
     19/6 * np.sin(17/11 - 3 * t) +
     263/5 * np.sin(t + 11/7) +
     614/15 * np.sin(2 * t + 11/7) +
     87/10 * np.sin(4 * t + 11/7) +
     1/7 * np.sin(5 * t + 11/8) +
     19/11 * np.sin(6 * t + 11/7) +
     7/5 * np.sin(7 * t + 11/7) +
     4/3 * np.sin(8 * t + 8/5) +
     9/5 * np.sin(10 * t + 14/9) +
     4/7 * np.sin(12 * t + 8/5) +
     3/11 * np.sin(13 * t + 3/2) +
     1/8 * np.sin(14 * t + 22/15) +
     1/9 * np.sin(15 * t + 12/7) +
     6/5 * np.sin(16 * t + 11/7) +
     2/9 * np.sin(18 * t + 11/7) +
     3/5 * np.sin(19 * t + 8/5) +
     1/26 * np.sin(21 * t + 15/11) +
     6/7 * np.sin(22 * t + 8/5) -
     1867/8) * _UnitStep(47 * np.pi - t) * _UnitStep(t - 43 * np.pi) +
     (118/39 * np.sin(t + 11/7) +
     40/7 * np.sin(2 * t + 33/7) +
     49/25 * np.sin(3 * t + 14/3) +
     12/5 * np.sin(4 * t + 8/5) +
     1/9 * np.sin(5 * t + 32/13) +
     5/2 * np.sin(6 * t + 13/8) +
     2/5 * np.sin(7 * t + 22/5) +
     3/4 * np.sin(8 * t + 7/4) -
     143/10) * _UnitStep(43 * np.pi - t) * _UnitStep(t - 39 * np.pi) +
     (-1/8 * np.sin(2/3 - 8 * t) -
     1/2 * np.sin(7/5 - 2 * t) -
     246/19 * np.sin(1/7 - t) +
     1/4 * np.sin(3 * t + 33/16) +
     1/6 * np.sin(4 * t + 17/6) +
     1/5 * np.sin(5 * t + 31/7) +
     1/11 * np.sin(6 * t + 50/17) +
     1/8 * np.sin(7 * t + 30/7) +
     665/6) * _UnitStep(39 * np.pi - t) * _UnitStep(t - 35 * np.pi) +
     (-119/10 * np.sin(7/15 - t) +
     2/11 * np.sin(2 * t + 25/7) +
     2/9 * np.sin(3 * t + 5/8) +
     1/5 * np.sin(4 * t + 33/7) +
     1/4 * np.sin(5 * t + 19/10) +
     1023/10) * _UnitStep(35 * np.pi - t) * _UnitStep(t - 31 * np.pi) +
     (-1/7 * np.sin(2/7 - 12 * t) -
     1/8 * np.sin(3/10 - 5 * t) +
     25/7 * np.sin(t + 77/17) +
     355/59 * np.sin(2 * t + 41/40) +
     27/5 * np.sin(3 * t + 46/15) +
     33/7 * np.sin(4 * t + 11/3) +
     27/10 * np.sin(6 * t + 13/9) +
     5/11 * np.sin(7 * t + 11/5) +
     5/8 * np.sin(8 * t + 3) +
     8/5 * np.sin(9 * t + 16/15) +
     16/15 * np.sin(10 * t + 1/7) +
     7/9 * np.sin(11 * t + 12/5) -
     862/7) * _UnitStep(31 * np.pi - t) * _UnitStep(t - 27 * np.pi) +
     (-1/3 * np.sin(5/4 - 8 * t) -
     2/5 * np.sin(5/9 - 7 * t) -
     5/7 * np.sin(11/8 - 5 * t) -
     7/2 * np.sin(15/14 - 2 * t) +
     29/8 * np.sin(t + 41/10) +
     11/6 * np.sin(3 * t + 13/3) +
     7/6 * np.sin(4 * t + 1/27) +
     2/7 * np.sin(6 * t + 8/7) +
     1/9 * np.sin(9 * t + 9/5) +
     2/7 * np.sin(10 * t + 1/10) +
     201/5) * _UnitStep(27 * np.pi - t) * _UnitStep(t - 23 * np.pi) +
     (-4/11 * np.sin(8/9 - 12 * t) -
     10/7 * np.sin(19/13 - 10 * t) +
     623/3 * np.sin(t + 10/7) +
     39/5 * np.sin(2 * t + 10/11) +
     251/9 * np.sin(3 * t + 4/3) +
     5/7 * np.sin(4 * t + 4/3) +
     61/6 * np.sin(5 * t + 4/3) +
     14/9 * np.sin(6 * t + 23/7) +
     76/25 * np.sin(7 * t + 9/7) +
     3/4 * np.sin(8 * t + 1/4) +
     19/5 * np.sin(9 * t + 3/2) +
     17/6 * np.sin(11 * t + 6/5) +
     13/8 * np.sin(13 * t + 14/13) +
     8/9 * np.sin(14 * t + 17/6) +
     24/25 * np.sin(15 * t + 1/2) +
     1/6 * np.sin(16 * t + 13/8) +
     5/8 * np.sin(17 * t + 1) +
     1/7 * np.sin(18 * t + 18/17) +
     6/7 * np.sin(19 * t + 1) +
     1/4 * np.sin(20 * t + 4/9) +
     2/7 * np.sin(21 * t + 7/5) +
     1/3 * np.sin(22 * t + 8/7) +
     2/5 * np.sin(23 * t + 1/26) +
     2/11 * np.sin(24 * t + 8/7) -
     243/8) * _UnitStep(23 * np.pi - t) * _UnitStep(t - 19 * np.pi) +
     (-111/10 * np.sin(4/5 - 9 * t) -
     12/5 * np.sin(7/13 - 2 * t) +
     1/6 * np.sin(t + 48/11) +
     13/8 * np.sin(3 * t + 27/7) +
     71/24 * np.sin(4 * t + 6/11) +
     22/9 * np.sin(5 * t + 7/2) +
     19/7 * np.sin(6 * t + 8/17) +
     20/7 * np.sin(7 * t + 34/9) +
     55/7 * np.sin(8 * t + 6/5) +
     64/9 * np.sin(10 * t + 38/9) +
     27/5) * _UnitStep(19 * np.pi - t) * _UnitStep(t - 15 * np.pi) +
     (-22/7 * np.sin(4/3 - 8 * t) -
     19/7 * np.sin(20/13 - 6 * t) +
     38/13 * np.sin(t + 1/24) +
     12/11 * np.sin(2 * t + 5/9) +
     26/7 * np.sin(3 * t + 7/9) +
     11/5 * np.sin(4 * t + 12/11) +
     37/10 * np.sin(5 * t + 17/10) +
     51/10 * np.sin(7 * t + 10/3) +
     33/4 * np.sin(9 * t + 26/7) +
     41/5 * np.sin(10 * t + 9/5) -
     27/2) * _UnitStep(15 * np.pi - t) * _UnitStep(t - 11 * np.pi) +
     (-172/5 * np.sin(3/8 - t) +
     5/4 * np.sin(2 * t + 7/2) +
     2303/24) * _UnitStep(11 * np.pi - t) * _UnitStep(t - 7 * np.pi) +
     (441/5 - 455/12 * np.sin(7/9 - t)) * _UnitStep(7 * np.pi - t) * _UnitStep(t - 3 * np.pi) +
     (-1/3 * np.sin(1/20 - 18 * t) -
     7/5 * np.sin(7/9 - 17 * t) -
     18/11 * np.sin(2/5 - 14 * t) -
     24/5 * np.sin(1/13 - 9 * t) +
     2767/7 * np.sin(t + 11/3) +
     229/5 * np.sin(2 * t + 17/7) +
     313/8 * np.sin(3 * t + 22/5) +
     32/3 * np.sin(4 * t + 22/5) +
     169/6 * np.sin(5 * t + 21/8) +
     23/7 * np.sin(6 * t + 26/11) +
     21/2 * np.sin(7 * t + 5/6) +
     55/6 * np.sin(8 * t + 14/5) +
     212/13 * np.sin(10 * t + 24/7) +
     26/9 * np.sin(11 * t + 9/2) +
     16/5 * np.sin(12 * t + 25/6) +
     35/17 * np.sin(13 * t + 4/11) +
     15/8 * np.sin(15 * t + 7/10) +
     2/3 * np.sin(16 * t + 20/9) +
     16/7 * np.sin(19 * t + 4/5) +
     13/7 * np.sin(20 * t + 29/7) +
     14/3 * np.sin(21 * t + 7/5) +
     4/3 * np.sin(22 * t + 7/4) +
     12/7 * np.sin(23 * t + 34/33) +
     7/4 * np.sin(24 * t + 27/7) -
     211/5) * _UnitStep(3 * np.pi - t) * _UnitStep(t + np.pi)) * _UnitStep(np.sqrt(np.sign(np.sin(t/2))))).real

def get_x_y():
    t = np.arange(0, 52 * np.pi, 0.0025, dtype=np.complex128)
    return _x(t), _y(t)
