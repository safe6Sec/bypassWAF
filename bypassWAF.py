# coding=utf-8
# author :safe6
# date:2021.1.23

import random


def bypass(payload):
    chars1 = ['%01', '%02', '%03', '%04', '%05', '%06', '%07', '%08', '%09', '%0A', '%0B', '%0C', '%0D', '%0E', '%0F',
              '%10', '%11',
              '%12', '%13', '%14', '%15', '%16', '%17', '%18', '%19', '%1A', '%1B', '%1C', '%1D', '%1E', '%1F', '%20']

    chars2 = ["/**/", "/*!*/", "/*!safe6*/", "+"]

    v = random.choice(chars1)
    payload = payload.replace(" ", random.choice(chars2))
    payload = payload.replace("=", v + "=" + v)
    payload = payload.replace("AND", v + "AND" + v)
    payload = payload.replace("and", v + "AND" + v)
    payload = payload.replace("WHERE", v + "WHERE" + v)
    payload = payload.replace("where", v + "where" + v)
    payload = payload.replace("UNION", "u%u006eion")
    payload = payload.replace("union", "u%u006eion")
    payload = payload.replace("CHAR", "%u0063har")
    payload = payload.replace("char", "%u0063har")
    payload = payload.replace("(", "+(")
    payload = payload.replace(".", ".+")
    payload = payload.replace("--", "/*!*/--")
    payload = payload.replace("SELECT", "se%u006cect")
    payload = payload.replace("select", "se%u006cect")
    payload = payload.replace("FROM", "%u0066rom")
    payload = payload.replace("from", "%u0066rom")

    print(payload)


if __name__ == '__main__':
    while True:
        payload = input("输入payload:")
        if payload == 'q':
            exit(0)
        if payload:
            bypass(payload)
