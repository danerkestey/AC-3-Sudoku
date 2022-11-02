import React from "react";
import { FormControl } from "react-bootstrap";

type IProps = {
  id: string;
  value: string;
  disabled: boolean;
  style: React.CSSProperties | undefined;
  onChange: any;
};

const Square: React.FC<IProps> = ({ id, value, disabled, style, onChange }) => {
  return (
    <FormControl
      className="square"
      id={id}
      type="text"
      value={value}
      onChange={(e) => onChange(e, id)}
      disabled={disabled}
      maxLength={1}
      style={style}
    />
  );
};

export default Square;
