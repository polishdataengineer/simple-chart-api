"""A simple API that returns two chart types (Pie and Bar)"""
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from plotly.offline import plot

from chart_generators.bar_chart import bar_chart_generation
from chart_generators.pie_chart import pie_chart_generation

app = FastAPI()


@app.post("/chart")
async def create_chart(data: dict) -> FileResponse:
  """This method will print the generated chart"""
  try:
    # Checking of the passed type
    chart_type = data["data"][0]["type"]
    if chart_type == "pie":
      fig = await pie_chart_generation(data)
    elif chart_type == "bar":
      fig = await bar_chart_generation(data)
  except Exception as e:
    raise HTTPException(status_code=501,
                        detail="Chart type is not implemented") from e

  try:
    # Apply the title
    fig.update_layout(title=data["title"])

    # Save the chart to a file
    chart = plot(fig, output_type="file")

    # Return the chart file as the response
    return FileResponse(chart, media_type="image/png")
  except Exception as e:
    raise HTTPException(status_code=503,
                        detail="Unable to generate media") from e
