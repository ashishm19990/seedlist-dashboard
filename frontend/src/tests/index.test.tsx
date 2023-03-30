import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders blank demo page', () => {
  render(<App />);
  expect(screen.findByRole('container')).toBeTruthy();
});
