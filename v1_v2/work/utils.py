import environment as env
import logging
import sshtunnel
import os
import psycopg2
import pandas as pd
import datetime
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
from pytz import timezone

def open_ssh_tunnel(username, password, host, bind_host, bind_port):
    sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    tunnel = SSHTunnelForwarder(
        (host, 22),
        ssh_username = username,
        ssh_password = password,
        remote_bind_address = (bind_host, bind_port)
    )
    
    tunnel.start()
    return tunnel
# ==========================

def mysql_connect(username, password, host, dbport, dbname):
    url = "mysql+pymysql://"+username+":"+password+"@"+host+":"+str(dbport)+"/"+dbname
    
    return create_engine(url, echo=True)
# ==========================

def postgres_connect(username, password, host, dbport, dbname):
    # params = {
    #     'database': dbname,
    #     'user': username,
    #     'password': password,
    #     'host': host,
    #     'port': dbport
    # }
    # conn = psycopg2.connect(**params)
    # curs = conn.cursor()
    # print("DB connected")
    # return conn

    url = 'postgresql+psycopg2://'+username+':'+password+'@'+host+':'+str(dbport)+'/'+dbname
    return create_engine(url, pool_recycle=3600)


# ==========================

def run_query(sql, connection):
    return pd.read_sql_query(sql, connection)
# ==========================

def tenant_exists(tenant):
    return env.tenants_to_shopping[tenant] if tenant in env.tenants_to_shopping else tenant
# ==========================

def get_key(obj, value):
    return [k for k, v in obj.items() if v == value][0]
# ==========================

def get_tenant(shopping_id):
    return get_key(env.tenants_to_shopping, env.current_shopping)
# ==========================

def add_timezone_to_date(sourceDate, timezoneName = 'America/Sao_Paulo'):
    customDate = None
    if (isinstance(sourceDate, str)):
        customDate = datetime.date.fromisoformat(datetime)
        
    elif (sourceDate == None):
        return None

    else:
        customDate = sourceDate

    brazilTimezone = timezone(timezoneName)
    customDate = brazilTimezone.localize(customDate)
    return customDate.strftime("%Y-%m-%d %H:%M:%S %z")
# ==========================
    
































