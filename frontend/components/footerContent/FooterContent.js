import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const FooterContent = () => {
  return (
    <Container>
      <Row className="justify-content-center">
        <Col xs="auto">
          Built with{' '}
          <span role="img" aria-label="heart">
            ❤️️
          </span>{' '}
          by{' '}
          <a href="/" style={{ fontWeight: 'bold' }}>
            NUSStatSoc
          </a>
        </Col>
      </Row>
      <Row className="justify-content-center mt-4">
        <Col xs="auto" className="text-center ml-md-3 mr-md-3">
          <a href="/">Contact</a>
        </Col>
        <Col xs="auto" className="text-center ml-md-3 mr-md-3">
          <a href="/">About</a>
        </Col>
        <Col xs="auto" className="text-center ml-md-3 mr-md-3">
          <a href="/">GitHub</a>
        </Col>
      </Row>
    </Container>
  );
};

export default FooterContent;
