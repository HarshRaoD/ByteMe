import React from 'react'
import './home.css'
import Card from 'react-bootstrap/Card';
import nltk from './nltk.png'
import t5 from './t5.png'

const Home = () => {
  return (
    <>
      <div className='title'>
        <h2>Studying research papers made easier!</h2>
        Some of the technologies we use:
      </div>

      <div className='card-container'>
      <Card style={{ width: '18rem' }} className='card'>
        <Card.Img variant="top" src={nltk} className='imageone' />
        <Card.Body>
          <Card.Text className='center'>
          The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English
          </Card.Text>
        </Card.Body>
      </Card>

      <Card style={{ width: '18rem' }} className='card'>
        <Card.Img variant="top" src={t5} className='image2' />
        <Card.Body>
          <Card.Text className='center'>
          T5, or Text-to-Text Transfer Transformer, is a Transformer based architecture that uses a text-to-text approach.
          </Card.Text>
        </Card.Body>
      </Card>
      
      </div>
    </>
  )
}

export default Home