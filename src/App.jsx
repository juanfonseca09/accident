import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col, Card } from "react-bootstrap";
import { FaGithub } from "react-icons/fa";
import "./App.css";

export default function App() {
  return (
    <div className="app-bg">
      <Container className="py-5">

        {/* HEADER */}
        <Row className="mb-5 text-center text-white">
          <Col>
            <h1 className="fw-bold text-uppercase">
              Análisis de Siniestros de Tránsito
            </h1>
          </Col>
        </Row>

        {/* CONTENIDO */}
        <Row className="mb-4 justify-content-center">
          <Col md={8}>
            <Card className="project-card shadow-sm border-0">
              <Card.Body>

                <p className="text-muted">
                  Este proyecto analiza datos de fallecidos en siniestros de tránsito en Uruguay para identificar patrones temporales y geográficos.
                </p>

                <p className="text-muted">
                  Se realizó limpieza de datos, transformación de variables y consultas con SQLite para agrupar la información y generar visualizaciones.
                </p>

                <p className="text-muted">
                  Se identifican picos hacia fin de año, mayor concentración en Montevideo y Canelones, y mayor incidencia en horarios de la tarde-noche.
                </p>

                <p className="text-muted mb-3">
                  También se observa una diferencia marcada por sexo, con predominio de casos en hombres.
                </p>

                {/* BOTÓN GITHUB */}
                <a
                  href="link.com"
                  target="_blank"
                  rel="noreferrer"
                  className="github-btn"
                >
                  <FaGithub style={{ marginRight: "6px" }} />
                  Ver código
                </a>

              </Card.Body>
            </Card>
          </Col>
        </Row>

        {/* IMAGEN */}
        <Row className="mb-5 d-flex justify-content-center">
          <Col md={3} className="text-center">
            <img src="/ccccc.png" alt="grafico" className="img-fluid rounded" />
          </Col>
        </Row>

      </Container>
    </div>
  );
}