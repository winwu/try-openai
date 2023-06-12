# AppHeader Component

The `AppHeader` component is a React component that renders a header for the application. It contains a menu button that toggles a dropdown menu, a logo, and a theme switch. The component also has two functions that handle the menu button click events: `toToggleMenu` and `goToBookmarks`. Additionally, it has a function that handles the click event for the "Clear Answer Records" button: `localstorageClean`.

## Props

The `AppHeader` component does not accept any props.

## State

The `AppHeader` component has one state variable:

- `showMenu`: A boolean value that determines whether the dropdown menu is visible or not.

## Functions

### toToggleMenu

The `toToggleMenu` function is called when the menu button is clicked. It toggles the `showMenu` state variable, which controls the visibility of the dropdown menu.

#### Input

- `e`: A SyntheticEvent object that represents the click event.

#### Output

None.

### goToBookmarks

The `goToBookmarks` function is called when the "Bookmarks List" button is clicked. It toggles the `showMenu` state variable and navigates to the bookmarks page using the `history` object from the `react-router-dom` library.

#### Input

- `e`: A SyntheticEvent object that represents the click event.

#### Output

None.

### localstorageClean

The `localstorageClean` function is called when the "Clear Answer Records" button is clicked. It displays a confirmation dialog and clears the answer records if the user confirms.

#### Input

- `e`: A SyntheticEvent object that represents the click event.

#### Output

None.

## Usage

To use the `AppHeader` component, import it into your React component and render it as follows:

```jsx
import AppHeader from './AppHeader';

function MyComponent() {
  return (
    <div>
      <AppHeader />
      {/* Your content here */}
    </div>
  );
}
```

The `AppHeader` component does not accept any props, so you can simply render it as shown above.