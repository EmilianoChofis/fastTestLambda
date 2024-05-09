import json

from hello_world.common.utils import db_connection


# import requests


def lambda_handler(event, context):

    """
    :param event:
    :param context:
    :return:
    """
    group = event['group']
    grade = event['grade']

    connection = db_connection()

    try:
        with connection.cursor() as cursor:
            sql = f"DELETE alumnos WHERE grade = {grade} and group={group}"
            cursor.execute(sql, (grade, group))
            connection.commit()
            return {
                'statusCode': 200,
                'body': json.dumps("Eliminado")
            }

    finally:
        connection.close()

