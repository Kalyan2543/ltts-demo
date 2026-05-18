import axios from 'axios';

const api = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const registerUser = async (data) => {
  const response = await api.post('/auth/register', data);
  return response.data;
};

export const loginUser = async (data) => {
  const response = await api.post('/auth/login', data);
  return response.data;
};

export const getProducts = async (params = {}) => {
  const response = await api.get('/products', { params });
  return response.data;
};

export const getCategories = async () => {
  const response = await api.get('/categories');
  return response.data;
};

export const getCart = async () => {
  const response = await api.get('/cart');
  return response.data;
};

export const addToCart = async (productId, quantity = 1) => {
  const response = await api.post('/cart', { product_id: productId, quantity });
  return response.data;
};

export const removeFromCart = async (itemId) => {
  const response = await api.delete(`/cart/${itemId}`);
  return response.data;
};

export const getReviews = async (productId) => {
  const response = await api.get('/reviews', { params: { product_id: productId } });
  return response.data;
};

export const subscribeNewsletter = async (email) => {
  const response = await api.post('/newsletter/subscribe', { email });
  return response.data;
};

export const getHeroBanners = async () => {
  const response = await api.get('/hero-banner');
  return response.data;
};

export const getSitemap = async () => {
  const response = await api.get('/sitemap');
  return response.data;
};

export default api;
