
from django.http import HttpResponse
from django.shortcuts import render

# -------------------------------------------------------------------------------------------
# 메인 페이지
def main(request):
    return render(request,
           'surveyapp/main.html',
           {})
# -------------------------------------------------------------------------------------------
# Part1_01 연도별 최저임금 현황
def part1_01(request):
    return render(request,
           'surveyapp/part1_01.html',
           {})
# -------------------------------------------------------------------------------------------
# Part1_02 연도별 물가 현황    
def part1_02(request):
    return render(request,
           'surveyapp/part1_02.html',
           {})
# -------------------------------------------------------------------------------------------
# Part1_01 연도별 GDP 현황
def part1_03(request):
    return render(request,
           'surveyapp/part1_03.html',
           {})
# -------------------------------------------------------------------------------------------