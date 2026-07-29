from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post("/cia/sql-analyst")
def sql_analyst():
    question = request.json.get("question")

    sql = vn.generate_sql(question)
    result = vn.run_sql(sql)

    return jsonify({
        "question": question,
        "sql": sql,
        "result": result.to_dict(orient="records")
    })

if __name__ == "__main__":
    app.run(debug=True)