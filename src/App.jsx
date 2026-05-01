import { Container, Row, Col, Card } from "react-bootstrap";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

export default function App() {

  const code = `
data = pd.read_csv("fallecidos-nueva-2019.csv", encoding="latin-1")
data.columns = data.columns.str.strip().str.upper()
data["FECHAYHORA"] = pd.to_datetime(data["FECHAYHORA"], errors="coerce")
data["mes"] = data["FECHAYHORA"].dt.month
data["hora"] = data["FECHAYHORA"].dt.hour
db = sqlite3.connect("fallecidos.db")
data.to_sql("fallecidos", db, if_exists="replace", index=False)
consulta = """
SELECT mes, COUNT(*) as total
FROM fallecidos
GROUP BY mes
ORDER BY mes
"""
res = pd.read_sql(consulta, db)
db.close()
`;

  return (
    <div>
      <Container className="py-5">
        <Row className="mb-5 text-center">
          <Col>
            <h1 className="fw-bold text-uppercase">
              Análisis de Siniestros de Tránsito
            </h1>
          </Col>
        </Row>
        <Row className="mb-4 justify-content-center">
          <Col md={8}>
            <Card className="shadow-sm border-0">
              <Card.Body>
                <p className="text-muted">
                  Este proyecto lo hice para analizar datos de fallecidos en siniestros de tránsito en Uruguay y tratar de entender si había algún patrón claro en los datos.
                </p>
                <p className="text-muted">
                  Primero cargué el dataset y armé algunas columnas como mes y hora a partir de la fecha, después usé SQLite para hacer consultas simples y agrupar la información, y con eso generé los gráficos.
                </p>
                <p className="text-muted">
                  Mirando los resultados se ven algunas cosas interesantes, por ejemplo, hay un pico bastante claro hacia fin de año, con diciembre siendo el mes con más casos y también aparecen valores relativamente altos en marzo, abril y junio.
                </p>
                <p className="text-muted">
                  A nivel geográfico, Montevideo y Canelones concentran la mayor cantidad de fallecidos, lo cual tiene bastante sentido por la cantidad de población y movimiento que tienen.
                </p>
                <p className="text-muted">
                  En cuanto a horarios, los valores más altos están en la tarde-noche, especialmente entre las 18 y las 20 horas, que coincide con momentos de mayor circulación y también hay algunos picos más chicos en la madrugada.
                </p>
                <p className="text-muted mb-0">
                  Por último, la diferencia por sexo es bastante marcada, con una mayoría clara de hombres sobre mujeres, en general, la idea fue más entender cómo se comportan los datos que hacer algo complejo.
                </p>
              </Card.Body>
            </Card>
          </Col>
        </Row>
        <Row className="mb-5 d-flex justify-content-center">
          <Col md={2} className="text-center">
            <img src="/ccccc.png" alt=''/>
          </Col>
        </Row>
        <Row>
          <Col>
            <Card className="shadow-sm border-0">
              <Card.Body>
                <SyntaxHighlighter language="python" style={oneDark}>
                  {code}
                </SyntaxHighlighter>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}