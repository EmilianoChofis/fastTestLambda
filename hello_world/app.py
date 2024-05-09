import json

from hello_world.common.utils import db_connection

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
            sql = "DELETE FROM alumnos WHERE grado = %s AND grupo = %s"
            cursor.execute(sql, (grade, group))
            connection.commit()
            return {
                'statusCode': 200,
                'body': json.dumps("Registro eliminado")
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
    finally:
        connection.close()
