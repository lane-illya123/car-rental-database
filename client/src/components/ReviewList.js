import { useState, useEffect } from 'react';
import NavBar from './NavBar';
import Reviews from './Reviews';
import ReviewForm from './ReviewForm';

function ReviewList() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/review")
      .then(r => r.json())
      .then(reviews => setReviews(reviews))
      .catch(error => console.error(error));
  }, []);

  function handleNewReview(newReview) {
    setReviews([...reviews, newReview]);
  }

  function handleUpdateReview(updatedReview) {
    const updatedReviews = reviews.map((review) =>
      review.id === updatedReview.id ? updatedReview : review
    );
    setReviews(updatedReviews);
  }

  function handleDeleteReview(deletedReview) {
    const updatedReview = reviews.filter((item) => item.id !== deletedReview.id);
    setReviews(updatedReview);
  }

  return (
    <>
      <div className="list-link">
        REVIEWS:
        {reviews.map((item) => (
          <Reviews 
          key={item.id} 
          review={item} 
          onDeleteReview={handleDeleteReview} 
          onUpdateReview={handleUpdateReview}/>
        ))}
        <ReviewForm handleNewReview={handleNewReview} />
      </div>
    </>
  );
}

export default ReviewList;