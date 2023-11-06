from sqlalchemy import create_engine, exc, text
import json

# Connect to the database
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/flask")

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs;"))
        result_dict = []
        for row in result.all():
            result_dict.append(row._mapping)
        print(result_dict)
        return result_dict
    
def load_job_with_id(id):
    with engine.connect() as conn:
        query = f"SELECT * FROM jobs WHERE id = {id}"
        result = conn.execute(text(query)) 
        # return json.dumps([dict(r) for r in result])
        result_dict = []
        for row in result.all():
            result_dict.append(row._mapping)
        if(len(result_dict)==0):
            return None
        else:
            print(result_dict) 
            return result_dict
        # if(result == None):
        #     return None
        # else:
        #     result_dict = [row._mapping for row in result]
        #     print(result_dict)
        #     return result_dict


        # for row in result.all():
        #     result_dict.append(row._mapping)
        # print(result_dict)
        # return result_dict  


    #     # if(len(result_dict)==0):
    #     #     return None
    #     # else:
    #     #     return result_dict[0]._mapping



