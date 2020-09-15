import React from 'react';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Image from 'react-bootstrap/Image';

import styles from '../../styles/CardDetectionLog.module.scss';

const CardDetectionLog = ({ imageUrls }) => {
  return (
    <Card className={styles.detectionLogCard}>
      <Card.Body className={styles.detectionLogCardBody}>
        <Card.Title>Detection Log</Card.Title>
        <Card.Text>
          <strong>Violations detected:</strong> {imageUrls.length}
        </Card.Text>
        <Container className={styles.imageContainer}>
          <Row className="m-0 p-0">
            {imageUrls.map((url) => (
              <Col
                key={url}
                style={{ margin: 0, padding: 5 }}
                xs={4}
                sm={4}
                md={3}
                lg={2}
              >
                <Image
                  style={{
                    width: '100%',
                    objectFit: 'cover',
                  }}
                  src={url}
                />
              </Col>
            ))}
          </Row>
        </Container>
      </Card.Body>
    </Card>
  );
};

export default CardDetectionLog;
