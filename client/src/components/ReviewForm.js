import {useState} from "react";
import { useFormik } from 'formik';
import * as Yup from 'yup';


function ReviewForm({ handleNewReview }) {
  const formik = useFormik({
    initialValues: {
      review: '',
    },
    validationSchema: Yup.object({
      review: Yup.string().required('Review is required'),
    }),
    onSubmit: (values) => {
      const formData = {
        description: values.review,
      };

      fetch('http://127.0.0.1:5555/review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
        .then((response) => response.json())
        .then((newItem) => handleNewReview(newItem));
    },
  });

  return (
    <div>
      <h2>Write a new review:</h2>
      <form className="formClass" onSubmit={formik.handleSubmit}>
        <label>New Review:</label>
        <input
          type="text"
          name="review"
          value={formik.values.review}
          onChange={formik.handleChange}
        />
        {formik.errors.review && formik.touched.review && (
          <div>{formik.errors.review}</div>
        )}

        <button type="submit">Add Review</button>
      </form>
    </div>
  );
}

export default ReviewForm;