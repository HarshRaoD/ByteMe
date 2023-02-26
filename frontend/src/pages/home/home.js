import React from 'react'
import './home.css'
import Card from 'react-bootstrap/Card';

const Home = () => {
  return (
    <div className='title'>
      <h2>Studying research papers made easier!</h2>
      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src="./nltk.png" />
        <Card.Body>
          <Card.Title>Card Title</Card.Title>
          <Card.Text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </Card.Text>
        </Card.Body>
      </Card>
    </div>
  )
}

export default Home