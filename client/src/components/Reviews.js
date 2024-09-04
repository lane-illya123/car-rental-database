import React from 'react'


function Reviews({review, onDeleteReview, onUpdateReview}){

    function handleDeleteReview() {
        fetch(`http://127.0.0.1:5555/review${review.id}`, {
          method: "DELETE",
        })
          .then((r) => r.json())
          .then(() => onDeleteReview(review));
      };

      function handleUpdateReview() {
        // Implement the PATCH request to update the review here
        const updatedReview = { ...review, /* Add updated fields */ };
        fetch(`http://127.0.0.1:5555/review/${review.id}`, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(updatedReview),
        })
          .then((response) => response.json())
          .then((updatedReview) => onUpdateReview(updatedReview));
      }

return(
<>
<div className = 'cards'>
    <p>{review.description}</p>
    <p>Created At:{review.created_at} Updated At:{review.updated_at}</p>
    <button onClick={handleUpdateReview}>Update Review</button>
    <button onClick={handleDeleteReview}>Delete Review</button>
</div>
</>
);
}

export default Reviews;