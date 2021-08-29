import {
  PRODUCT_CREATE_FAIL,
  PRODUCT_CREATE_REQUEST,
  PRODUCT_CREATE_RESET,
  PRODUCT_CREATE_SUCCESS,
  PRODUCT_DELETE_FAIL,
  PRODUCT_DELETE_REQUEST,
  PRODUCT_DELETE_RESET,
  PRODUCT_DELETE_SUCCESS,
  PRODUCT_DETAIL_FAIL,
  PRODUCT_DETAIL_REQUEST,
  PRODUCT_DETAIL_SUCCESS,
  PRODUCT_LIST_FAIL,
  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_RELATED_FAIL,
  PRODUCT_RELATED_REQUEST,
  PRODUCT_RELATED_RESET,
  PRODUCT_RELATED_SUCCESS,
  PRODUCT_UPDATE_FAIL,
  PRODUCT_UPDATE_REQUEST,
  PRODUCT_UPDATE_RESET,
  PRODUCT_UPDATE_SUCCESS,
} from "../constants/productConstants";

export const productsReducer = (
  state = { products: [], loading: true },
  action
) => {
  switch (action.type) {
    case PRODUCT_LIST_REQUEST:
      return { loading: true };
    case PRODUCT_LIST_SUCCESS:
      return {
        loading: false,
        products: action.payload.listProducts,
        pages: action.payload.pages,
        page: action.payload.page,
        totalProducts: action.payload.count,
      };
    case PRODUCT_LIST_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};

export const productsRelatedReducer = (
  state = { productsRelated: [], loading: false },
  action
) => {
  switch (action.type) {
    case PRODUCT_RELATED_REQUEST:
      return { loading: true };
    case PRODUCT_RELATED_SUCCESS:
      return {
        loading: false,
        productsRelated: action.payload,
        pages: action.payload.pages,
        page: action.payload.page,
        totalProducts: action.payload.count,
      };
    case PRODUCT_RELATED_FAIL:
      return { loading: false, error: action.payload };
    case PRODUCT_RELATED_RESET:
      return { };
    default:
      return state;
  }
};

export const productDetailsReducer = (
  state = { products: {}, loading: true },
  action
) => {
  switch (action.type) {
    case PRODUCT_DETAIL_REQUEST:
      return { loading: true };
    case PRODUCT_DETAIL_SUCCESS:
      return { loading: false, success: true, product: action.payload };
    case PRODUCT_DETAIL_FAIL:
      return { loading: false, success: false, error: action.payload };
    default:
      return state;
  }
};

export const productCreateReducer = (state = { product: {} }, action) => {
  switch (action.type) {
    case PRODUCT_CREATE_REQUEST:
      return { loading: true };
    case PRODUCT_CREATE_SUCCESS:
      return { loading: false, success: true, product: action.payload };
    case PRODUCT_CREATE_FAIL:
      return { loading: false, success: false, error: action.payload };
    case PRODUCT_CREATE_RESET:
      return {};
    default:
      return state;
  }
};

export const productUpdateReducer = (state = {}, action) => {
  switch (action.type) {
    case PRODUCT_UPDATE_REQUEST:
      return { loading: true };
    case PRODUCT_UPDATE_SUCCESS:
      return { loading: false, success: true };
    case PRODUCT_UPDATE_FAIL:
      return { loading: false, success: false, error: action.payload };
    case PRODUCT_UPDATE_RESET:
      return {};
    default:
      return state;
  }
};

export const productDeleteReducer = (state = {}, action) => {
  switch (action.type) {
    case PRODUCT_DELETE_REQUEST:
      return { loading: true };
    case PRODUCT_DELETE_SUCCESS:
      return { loading: false, success: true };
    case PRODUCT_DELETE_FAIL:
      return { loading: false, success: false, error: action.payload };
    case PRODUCT_DELETE_RESET:
      return {};
    default:
      return state;
  }
};